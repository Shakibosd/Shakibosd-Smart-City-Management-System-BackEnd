from rest_framework.views import APIView
from .serializers import PasswordChangeSerializer, PasswordResetRequestSerializer, RegisterSerializer,LoginSerializer
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Profile
from .serializers import ProfileSerializer
from django.core.mail import EmailMultiAlternatives
from django.utils.http import urlsafe_base64_decode
from rest_framework.permissions import IsAuthenticatedOrReadOnly

#user list dekhar jonno
class UserProfileListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user = Profile.objects.all()
        serializer = ProfileSerializer(user, many = True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#spacific user list dekhar jonno
class UserProfileDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        profile = get_object_or_404(Profile, user=user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        profile = get_object_or_404(Profile, user=user)

        serializer = ProfileSerializer(profile, data=request.data, partial=True)

        if serializer.is_valid():
            user_data = request.data.get("user", {})
            user.username = user_data.get("username", user.username)
            user.email = user_data.get("email", user.email)
            user.first_name = user_data.get("first_name", user.first_name)
            user.last_name = user_data.get("last_name", user.last_name)
            user.save()

            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#user account created
class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print(token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print(uid)
            confirm_link = f'https://smart-city-silk.vercel.app/authentication/active/{uid}/{token}/'
            email_subject = 'Confirm Your Email'
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
            return Response({'detail' : 'Check Your Email For Confirmation'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#user activat hobe link diye
def user_activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
        print(request)

    except (User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('https://smarts-city.netlify.app/login.html')
    else:
        return redirect('https://smarts-city.netlify.app/signup.html')       

#user je account create koreche ejonno se ekon web site e probesh korbe
class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']    
            password = serializer.validated_data['password']    
            user = authenticate(username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
#user website theke bahir hobe        
class LogoutAPIView(APIView):
    def get(self, request):
        user = request.user
        if hasattr(user, 'auth_token'):
            user.auth_token.delete()

        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

#user tar password ta jeno reset dite pare
class PasswordResetRequestAPIView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.validated_data['email'])
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk)) 
                reset_link = f'https://smarts-city.netlify.app/reset_password_form.html?uid64={uid}&token={token}'
                email_subject = 'Reset Your Password'
                email_body = render_to_string('reset_password_email.html', {'reset_link': reset_link})
                email = EmailMultiAlternatives(email_subject, '', to=[user.email])
                email.attach_alternative(email_body, 'text/html')
                email.send()
                return Response({'detail': 'Password reset link sent to your email.'}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#user tar password ta jeno reset er jonno confirm korte parbe
class PasswordChangeAPIView(APIView):
    def post(self, request, uid64, token):
        try:
            uid = urlsafe_base64_decode(uid64).decode()
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            serializer = PasswordChangeSerializer(data=request.data)
            if serializer.is_valid():
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response({'detail': 'Password has been changed successfully.'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid token or user.'}, status=status.HTTP_400_BAD_REQUEST)
    

    