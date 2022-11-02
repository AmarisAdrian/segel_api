from django.db import models
from app.config.models import *

# Create your models here.
class DivipolModel(models.Model):
    departamento = models.ForeignKey(DepartamentoModel, models.DO_NOTHING, db_column='departamento')
    ciudad = models.ForeignKey(CiudadModel, models.DO_NOTHING, db_column='ciudad')
    nombre = models.CharField(max_length=45)
    referencia = models.CharField(unique=True, max_length=60, blank=True, null=True)
    comentario = models.CharField(max_length=60, blank=True, null=True)
    active = models.BooleanField(db_column='active',blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.departamento 
    def __str__(self):
        return self.ciudad

    class Meta:
        managed = True
        db_table = 'divipol'
        verbose_name="Divipol"
        verbose_name_plural= 'Divipol' 