from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import PublicTransport
from .serializers import PublicTransportSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PublicTransport
from .serializers import PublicTransportSerializer

class PublicTransportAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        transports = PublicTransport.objects.all()
        serializer = PublicTransportSerializer(transports, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PublicTransportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransportDetailAPIView(APIView):
    def get(self, request, bus_id):
        try:
            transport = PublicTransport.objects.get(id=bus_id)
            serializer = PublicTransportSerializer(transport)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PublicTransport.DoesNotExist:
            return Response({"error": "Transport not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, bus_id):
        try:
            transport = PublicTransport.objects.get(id=bus_id)
        except PublicTransport.DoesNotExist:
            return Response({'error': 'Transport not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PublicTransportSerializer(transport, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, bus_id):
        try:
            transport = PublicTransport.objects.get(id=bus_id)
        except PublicTransport.DoesNotExist:
            return Response({'error': 'Transport not found.'}, status=status.HTTP_404_NOT_FOUND)

        transport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_transport(request, pk):
    transport_instance = get_object_or_404(PublicTransport, pk=pk)
    serializer = PublicTransportSerializer(instance=transport_instance, data=request.data, partial=True)  # Allow partial updates
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class UpdateLocationView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def post(self, request, bus_number):
        try:
            transport = PublicTransport.objects.get(bus_number=bus_number)
            transport.current_latitude = request.data.get('latitude')
            transport.current_longitude = request.data.get('longitude')
            transport.save()
            return Response({'status' : 'Location Update Successfully'})
        except PublicTransport.DoesNotExist:
            return Response({'error' : 'Bus Not Found'}, status=status.HTTP_404_NOT_FOUND)

 
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100        
    
    def get_paginated_response(self, data):
        return Response({
            'link' : {
                'next' : self.get_next_link(),
                'previous' : self.get_previous_link()
            },
            'count' : self.page.paginator.count,
            'results' : data
        })


class TransportListView(generics.ListAPIView):
    queryset = PublicTransport.objects.all()
    serializer_class = PublicTransportSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['route_name', 'bus_number']  
    search_fields = ['route_name', 'bus_number']     
    pagination_class = CustomPagination
    