from rest_framework import serializers
from app.divipol.models import *

class DivipolSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivipolModel
        fields = ['id', 'departamento', 'ciudad','nombre','referencia','comentario','active', 'created_at', 'updated_at']