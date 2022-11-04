from rest_framework import serializers
from app.zona_votacion.models import *

class ZonaVotacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZonaVotacionModel
        fields = ['id', 'divipol', 'numero','codigo','nombre','active','created_at', 'updated_at']