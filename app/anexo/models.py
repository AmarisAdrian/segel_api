from django.db import models
from app.usuario.models import *
from app.votante.models import *

# Create your models here.
class AnexoUsuarioModel(models.Model):
    usuario = models.ForeignKey(User ,on_delete=models.CASCADE)
    imagen = models.FileField(upload_to='soporte/',blank=False, null=False)
    comentario = models.CharField(max_length=100, blank=False, null=True)
    active = models.BooleanField(db_column='active',blank=False, null=False,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.usuario

    class Meta:
        managed = True
        db_table = 'anexo_usuario'
        verbose_name="Anexo usuario"
        verbose_name_plural= 'Anexo usuarios' 
        

class AnexoVotanteModel(models.Model):
    votante = models.ForeignKey(VotanteModel, on_delete=models.CASCADE, db_column='votante')
    imagen = models.FileField(upload_to='soporte/',blank=False, null=False)
    comentario = models.CharField(max_length=100, blank=False, null=False)
    active = models.BooleanField(db_column='active',blank=False, null=False,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.votante
    class Meta:
        managed = True
        db_table = 'anexo_votante'
        verbose_name="Anexo votante"
        verbose_name_plural= 'Anexo votantes' 