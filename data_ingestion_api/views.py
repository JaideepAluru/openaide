from django.shortcuts import render
from rest_framework import generics
from data_ingestion_api.models import Document
from .serializers import DocumentSerializer

class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

