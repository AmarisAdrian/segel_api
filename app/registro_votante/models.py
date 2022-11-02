from django.db import models
from app.puesto_votacion.models import *
from app.votante.models import *

class RegistroVotanteModel(models.Model):
    id = models.AutoField(primary_key=True)
    votante = models.OneToOneField(VotanteModel, on_delete=models.CASCADE, db_column='votante',unique=True)
    puesto = models.ForeignKey(PuestoVotacionModel,  on_delete=models.CASCADE, db_column='puesto')
    mesa = models.IntegerField(blank=True, null=True)
    comentario = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(db_column='active',blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.votante
        
    class Meta:
        managed = True
        db_table = 'registro_votante'
        verbose_name="registro votante"
        verbose_name_plural= 'registro votantes' 