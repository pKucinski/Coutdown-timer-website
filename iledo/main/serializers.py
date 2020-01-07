from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Photo, Date


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ['text', 'day', 'month', 'year', 'hour', 'minute', 'second']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['name', 'photo']