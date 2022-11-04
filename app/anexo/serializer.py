from rest_framework import serializers
from app.anexo.models import *

class AnexoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnexoUsuarioModel
        fields = ['id', 'usuario', 'imagen','comentario','active', 'created_at', 'updated_at']
        
        
class AnexoVotanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnexoVotanteModel
        fields = ['id', 'votante', 'imagen','comentario','active', 'created_at', 'updated_at']      