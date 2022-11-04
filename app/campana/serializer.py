from rest_framework import serializers
from app.campana.models import *

class CampanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampanaModel
        fields = ['id', 'nombre', 'eslogan','logo','partido','candidato','active', 'created_at', 'updated_at']