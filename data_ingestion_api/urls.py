from django.urls import path
from .views import DocumentListCreateView

urlpatterns = [
    path('Users/jaideepreddyaluru/Documents/dest/', DocumentListCreateView.as_view(), name='document-list-create'),
]