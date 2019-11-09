from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NoteSerializer, CategorySerializer
from .models import Note, Category

# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-date')
    serializer_class = NoteSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer