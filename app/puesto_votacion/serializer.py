from rest_framework import serializers
from app.puesto_votacion.models import *

class PuestoVotacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuestoVotacionModel
        fields = ['id', 'zona', 'codigo','nombre','direccion','mesa','potencial','active', 'created_at', 'updated_at']