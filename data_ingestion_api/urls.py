from django.urls import path
from .views import DocumentListCreateView,DownloadPDFView

urlpatterns = [
    path('Users/jaideepreddyaluru/Documents/dest/', DocumentListCreateView.as_view(), name='document-list-create'),
    path('Users/jaideepreddyaluru/Documents/dest/<int:document_id>/download/', DownloadPDFView.as_view(), name='download-pdf'),

]