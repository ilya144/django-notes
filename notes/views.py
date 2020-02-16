from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NoteSerializer, CategorySerializer, UserSerializer
from .models import Note, Category
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# API View Sets
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-date')
    serializer_class = NoteSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# API User Session control

@csrf_exempt
def register_view(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    
    serializer = UserSerializer( data=json.loads(request.body) )
    print(serializer.is_valid())
    # print(serializer.validated_data)
    if serializer.is_valid():
        print(serializer.create(serializer.validated_data))
    else:
        print(serializer._errors)

    return JsonResponse({"endpoint": "reg", "status": "ok"})

@csrf_exempt
def login_view(request):
    if request.method != 'POST':
        request.session["name"] = "test"
        return HttpResponseBadRequest()

    return JsonResponse({"endpoint": "login", "status": "ok"})

@csrf_exempt
def logout_view(request):
    if request.method != 'POST':
        request.session.flush()
        return HttpResponseBadRequest()

    return JsonResponse({"endpoint": "logout", "status": "ok"})
