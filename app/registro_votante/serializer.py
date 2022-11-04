from rest_framework import serializers
from app.registro_votante.models import *

class RegistroVotanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroVotanteModel
        fields = ['id', 'votante', 'puesto','mesa','comentario','active', 'created_at', 'updated_at']