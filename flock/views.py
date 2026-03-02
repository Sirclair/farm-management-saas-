from rest_framework import viewsets
from .models import FlockBatch, DailyRecord
from .serializers import FlockBatchSerializer, DailyRecordSerializer

class FlockBatchViewSet(viewsets.ModelViewSet):
    queryset = FlockBatch.objects.all()
    serializer_class = FlockBatchSerializer

class DailyRecordViewSet(viewsets.ModelViewSet):
    queryset = DailyRecord.objects.all()
    serializer_class = DailyRecordSerializer