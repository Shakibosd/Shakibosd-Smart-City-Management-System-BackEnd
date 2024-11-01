from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response

class IsAdminStatusAPIView(APIView):
    parser_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        user = request.user
        if user.is_staff:
            return Response({"is_admin" : True})
        return Response({"is_admin" : False})