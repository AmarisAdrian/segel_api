from django.db import models
from app.zona_votacion import *
from app.zona_votacion.models import ZonaVotacionModel
# Create your models here.
class PuestoVotacionModel(models.Model):
    zona = models.ForeignKey(ZonaVotacionModel,  on_delete=models.CASCADE, db_column='zona')
    codigo = models.CharField(max_length=150,unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    direccion = models.CharField(max_length=60, blank=False, null=False)
    mesa = models.IntegerField()
    potencial = models.IntegerField()
    active = models.BooleanField(db_column='active',blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.zona
        
    class Meta:
        managed = True
        db_table = 'puesto_votacion'
        verbose_name="puesto votacion"
        verbose_name_plural= 'puesto de votaciones' 