from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
import re


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=False)
    email = serializers.EmailField(source="user.email", read_only=False)
    first_name = serializers.CharField(source="user.first_name", read_only=False)
    last_name = serializers.CharField(source="user.last_name", read_only=False)
    
    class Meta:
        model = Profile
        fields = ['id', 'gender', 'religion', 'phone_number', 'age', 'date_of_birth', 'profile_img', 'username', 'email', 'first_name', 'last_name']
     
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None) 
        if user_data:
            # Update user fields
            user = instance.user
            user.username = user_data.get('username', user.username)
            user.email = user_data.get('email', user.email)
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.save()

        # Update profile fields
        instance.gender = validated_data.get('gender', instance.gender)
        instance.religion = validated_data.get('religion', instance.religion)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.age = validated_data.get('age', instance.age)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.profile_img = validated_data.get('profile_img', instance.profile_img)
        instance.save()

        return instance    


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    gender = serializers.ChoiceField(choices=Profile.GENDER_CHOICE, write_only=True)
    religion = serializers.ChoiceField(choices=Profile.RELIGION_CHOICES, write_only=True)
    phone_number = serializers.CharField(write_only=True)
    age = serializers.IntegerField(write_only=True)
    date_of_birth = serializers.DateTimeField(write_only=True)
    profile_img = serializers.URLField()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'gender', 'religion', 'phone_number', 'age', 'date_of_birth', 'profile_img']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        # Password validation
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match!")

        # Phone number validation
        phone_number = data.get('phone_number')
        if phone_number and not re.match(r'^\+?1?\d{9,15}$', phone_number):
            raise serializers.ValidationError("Phone number must be entered in the format: '+99999999'. Up to 15 digits allowed.")
         
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        profile_img = validated_data.pop('profile_img', None)
        gender = validated_data.pop('gender', None)
        religion = validated_data.pop('religion', None)
        phone_number = validated_data.pop('phone_number', None)
        age = validated_data.pop('age', None)
        date_of_birth = validated_data.pop('date_of_birth', None)

        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        
        user.is_active = False  
        user.save()

        Profile.objects.create(
            user=user,
            profile_img=profile_img,
            gender=gender,  
            religion=religion,
            phone_number=phone_number,
            age=age,
            date_of_birth=date_of_birth,
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)    
    password = serializers.CharField(required = True)    
    

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PasswordChangeSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data