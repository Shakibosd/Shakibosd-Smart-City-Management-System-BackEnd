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

class PublicTransportAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        transports = PublicTransport.objects.all()
        serializer = PublicTransportSerializer(transports, many=True)
        return Response(serializer.data)

class TransportDetailAPIView(APIView):
    def get(self, request, bus_id):
        try:
            transport = PublicTransport.objects.get(id=bus_id)
            serializer = PublicTransportSerializer(transport)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PublicTransport.DoesNotExist:
            return Response({"error": "Transport not found"}, status=status.HTTP_404_NOT_FOUND)
            

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
    