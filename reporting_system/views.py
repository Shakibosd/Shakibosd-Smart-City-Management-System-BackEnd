from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import IncidentReport
from .serializers import IncidetReportSerializer
from rest_framework.response import Response
from rest_framework import status

class IncidentReportAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        reports = IncidentReport.objects.all()
        serializer = IncidetReportSerializer(reports, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = IncidetReportSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)