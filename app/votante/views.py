from django.conf import settings
from django.db import models
from app.config.models import *
from app.campana.models import *
from app.usuario.models import *

# Create your models here.
class VotanteModel(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_documento = models.ForeignKey(TipoDocumentoModel, models.DO_NOTHING, db_column='tipo_documento')
    estado_usuario = models.ForeignKey(EstadoUsuarioModel, models.DO_NOTHING, db_column='estado_usuario')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    campana = models.ForeignKey(CampanaModel, models.DO_NOTHING, db_column='campana')
    nodocumento = models.BigIntegerField(unique=True ,db_column='nodocumento')
    nombre = models.CharField(max_length=45, db_column='nombre')
    apellido = models.CharField(max_length=45, db_column='apellido')
    genero = models.ForeignKey(GeneroModel, models.DO_NOTHING, db_column='genero')
    movil = models.IntegerField(blank=True, null=True, db_column='movil')
    fijo = models.IntegerField( blank=True, null=True, db_column='fijo')
    direccion = models.CharField(max_length=70, db_column='direccion')
    departamento = models.ForeignKey(DepartamentoModel, models.DO_NOTHING, db_column='departamento')
    ciudad = models.ForeignKey(CiudadModel, models.DO_NOTHING, db_column='ciudad')
    firma = models.FileField(upload_to='soporte/',blank=True, null=True)

    def __str__(self):
        return self.tipo_documento
    def __str__(self):
        return self.estado_usuario
    def __str__(self):
        return self.campana
    def __str__(self):
        return self.usuario
    def __str__(self):
        return self.genero
    def __str__(self):
        return self.departamento
    def __str__(self):
        return self.ciudad

    class Meta:
        managed = True
        db_table = 'votante'
        verbose_name="Votante"
        verbose_name_plural= 'Votantes' 