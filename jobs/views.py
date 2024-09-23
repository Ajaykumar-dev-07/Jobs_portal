from django.shortcuts import render
from rest_framework import viewsets
from .models import JobPost,Application
from .serializers import JobPostSerializer,ApplicationSerializer

class JobPostViewSet(viewsets.ModelViewSet):
    queryset=JobPost.objects.all()
    serializer_class=JobPostSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset=Application.objects.all()
    serializer_class=ApplicationSerializer

   


