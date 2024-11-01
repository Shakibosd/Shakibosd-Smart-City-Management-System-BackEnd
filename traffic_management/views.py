from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import TrafficUpdate
from .serializers import TrafficUpdateSerializer

class TrafficStatusAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        traffic_updates = TrafficUpdate.objects.all()
        serializer = TrafficUpdateSerializer(traffic_updates, many=True)
        return Response(serializer.data)
        
        