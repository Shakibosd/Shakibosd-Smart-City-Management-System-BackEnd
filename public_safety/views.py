from rest_framework.views import APIView
from .models import EmergencyService
from .serializers import EmergencyServiceSerializer
from rest_framework.response import Response

class EmergencyServiceAPIView(APIView):
    def get(self, request):
        service = EmergencyService.objects.all()
        serializer = EmergencyServiceSerializer(service, many=True)
        return Response(serializer.data)