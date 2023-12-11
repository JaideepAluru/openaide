from django.shortcuts import render
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from data_ingestion_api.models import Document
from .serializers import DocumentSerializer

class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DownloadPDFView(APIView):
    def get(self, request, document_id):
        document = get_object_or_404(Document, pk=document_id)
        file_path = document.file.path
        response = FileResponse(open(file_path, 'rb'))
        return response
