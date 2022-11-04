from rest_framework import serializers
from app.usuario.models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['tipo_documento', 'estado_usuario','campana','nodocumento','nombre','apellido', 'genero', 'movil', 'fijo', 'direccion', 'departamento', 'ciudad','firma']