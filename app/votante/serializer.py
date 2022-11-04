from rest_framework import serializers
from app.votante.models import *

class VotanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotanteModel
        fields = ['id', 'tipo_documento', 'estado_usuario','campana','nodocumento','nombre','apellido', 'genero', 'movil', 'fijo', 'direccion', 'departamento', 'ciudad','firma']