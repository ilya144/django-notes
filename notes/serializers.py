# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'