from app.models import *
from rest_framework import serializers

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actors
        fields='__all__'