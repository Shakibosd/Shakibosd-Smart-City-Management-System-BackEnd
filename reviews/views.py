from rest_framework.views import APIView
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework import generics 

class ReviewCreategenericsView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

class ReviewListAPIView(APIView):
     def get(self, request, transport__id):
        reviews = Review.objects.filter(transport__id=transport__id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)