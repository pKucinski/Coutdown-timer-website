from django.shortcuts import render
from django.shortcuts import render
from .models import Date, Photo
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, DateSerializer, PhotoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class DateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Date.objects.all()
    serializer_class = DateSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

def mainpage(request):
    date = Date.objects.all()
    photo = Photo.objects.all()
    return render(request, 'index.html', {'date':date, 'photo':photo})
