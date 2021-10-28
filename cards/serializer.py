from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User,Flashcards

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FlashcardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcards
        fields = '__all__'