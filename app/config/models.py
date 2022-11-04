from django.db import models

class DepartamentoModel(models.Model):
    nombre = models.CharField(max_length=150,db_column='nombre',blank=False, null=False)
    active = models.BooleanField(db_column='active',blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.nombre) 
    
    class Meta:
        managed = True
        db_table = 'departamento'
        verbose_name="Departamento"
        verbose_name_plural= 'Departamentos' 

class CiudadModel(models.Model):
    nombre = models.CharField(max_length=150,db_column='nombre',blank=False, null=False)
    departamento = models.ForeignKey(DepartamentoModel, models.DO_NOTHING, db_column='departamento')
    active = models.BooleanField(db_column='active',blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)   
    
    def __str__(self):
        return str(self.nombre) 
    
    class Meta:
        managed = True
        db_table = 'ciudad'
        verbose_name="ciudad"
        verbose_name_plural= 'ciudades' 

class ConfiguracionModel(models.Model):
    nombre = models.CharField(max_length=255,db_column='nombre',blank=False, null=False)
    manejador = models.CharField(max_length=50,db_column='manejador',blank=False, null=False)
    valor = models.CharField(max_length=255,db_column='valor',blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'configuracion'
        verbose_name="configuracion"
        verbose_name_plural= 'configuraciones' 


class LogModel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    modulo = models.CharField(db_column='modulo', max_length=300)
    request = models.CharField(db_column='request', max_length=800, null= True,blank=True)
    excepcion = models.CharField(db_column='excepcion', max_length=600)
    fecha_ingreso = models.DateTimeField(db_column='fecha_ingreso', auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'log'
        verbose_name="log"
        verbose_name_plural= 'logs' 

class EstadoUsuarioModel(models.Model):
    nombre = models.CharField(max_length=255, null= False,blank=False)
    active = models.BooleanField(db_column='active',blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.nombre)   
      
    class Meta:
        managed = True
        db_table = 'estado_usuario'
        verbose_name="estado usuario"
        verbose_name_plural= 'estado usuarios' 


class GeneroModel(models.Model):
    nombre = models.CharField(max_length=15, blank=False, null=False)
    active = models.BooleanField(db_column='active',blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.nombre)  
    
    class Meta:
        managed = True
        db_table = 'genero'
        verbose_name="genero"
        verbose_name_plural= 'generos' 

class TipoDocumentoModel(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)
    active = models.BooleanField(db_column='active',blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.nombre) 
    
    class Meta:
        managed = True
        db_table = 'tipo_documento'
        verbose_name="Tipo de documentos"
        verbose_name_plural= 'Tipo documentos' 

class TipoUsuarioModel(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)
    active = models.BooleanField(db_column='active',blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.nombre) 
    class Meta:
        managed = True
        db_table = 'tipo_usuario'
        verbose_name="Tipo usuario"
        verbose_name_plural= 'Tipo usuarios' 
