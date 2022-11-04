from rest_framework import serializers
from app.config.models import *

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartamentoModel
        fields = ['id', 'nombre', 'active', 'created_at', 'updated_at']
        
class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CiudadModel
        fields = ['id', 'nombre', 'departamento', 'active', 'created_at', 'updated_at']
        
class ConfiguracionSerializer(serializers.ModelSerializer):
   class Meta:
        model = ConfiguracionModel
        fields = ['id', 'nombre', 'manejador', 'valor']
        
class LogSerializer(serializers.ModelSerializer):
   class Meta:
        model = LogModel
        fields = ['id', 'modulo', 'request', 'excepcion', 'fecha_ingreso']
        
class EstadoUsuarioSerializer(serializers.ModelSerializer):
   class Meta:
        model = EstadoUsuarioModel
        fields = ['id', 'nombre', 'active', 'created_at', 'updated_at']
        
class GeneroSerializer(serializers.ModelSerializer):
   class Meta:
        model = GeneroModel
        fields = ['id', 'nombre', 'active', 'created_at', 'updated_at']
        
class TipoDocumentoSerializer(serializers.ModelSerializer):
   class Meta:
        model = TipoDocumentoModel
        fields = ['id', 'nombre', 'active', 'created_at', 'updated_at']
        
class TipoUsuarioSerializer(serializers.ModelSerializer):
   class Meta:
        model = TipoUsuarioModel
        fields = ['id', 'nombre', 'active', 'created_at', 'updated_at']