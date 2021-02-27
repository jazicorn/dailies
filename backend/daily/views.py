from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DailySerializer
from .models import Daily

# Create your views here.

class DailyView(viewsets.ModelViewSet):
    serializer_class = DailySerializer
    queryset = Daily.objects.all()
