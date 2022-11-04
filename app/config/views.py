from rest_framework.response import Response
from django.shortcuts import render
from app.config.models import *
from rest_framework import viewsets,status
from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from app.config.serializer import *
from app.config.response import *
# Create your views here.

class DepartamentoViewSet(viewsets.ModelViewSet):
   queryset = DepartamentoModel.objects.all()        
   serializer_class = DepartamentoSerializer
   model = DepartamentoModel 
   def create(self, request, format=None):
      module= "DepartamentoViewSet/create"
      try:
         serializer= DepartamentoSerializer(data = request.data,context={'request': request})
         if serializer.is_valid():
            serializer.save()
            response = ResponseData(module,"Departamento creado exitosamente",serializer.data,status.HTTP_201_CREATED)
            return Response(response, status.HTTP_201_CREATED)
         else:
           response = ResponseData(module,"Departamento no pudo ser creado",serializer.errors,status.HTTP_200_OK)  
           return Response(response, status=status.HTTP_200_OK)
      except Exception as ex:
         response = ResponseData(module,'Excepcion controlada: ' +str(ex) ,serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
         return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

   def partial_update(self,request,*args,**kwargs):
      if request.method == 'PATCH':
         module = "DepartamentoViewSet/partial_update"
         try:
            departamento = DepartamentoModel.objects.filter(id = kwargs['pk']).exists()
            if departamento :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = DepartamentoSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  with transaction.atomic():
                     serializer.save()
                     response =  ResponseData(module,"Departamento actualizado",serializer.data,status.HTTP_201_CREATED)  
               else:
                   response =  ResponseData(module,"Departamento no actualizado",serializer.errors,status.HTTP_200_OK)  
            else:
               response =  ResponseData(module,"Departamento no encontrado",serializer.errors,status.HTTP_200_OK)  
            return Response(response)
         except Exception as ex:
            response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
            return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   
   def update(self,request,*args,**kwargs):
      if request.method == 'PUT':
         module = "DepartamentoViewSet/update"
         try:
            producto = DepartamentoModel.objects.filter(id = kwargs['pk']).exists()
            if producto :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = DepartamentoSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  responseData = None
                  with transaction.atomic():
                     response =  ResponseData(module,"Departamento actualizado",serializer.data,status.HTTP_201_CREATED)  
                  return Response(response)
               else:
                  response =  ResponseData(module,"Deparamento no actualizado",serializer.errors,status.HTTP_200_OK)  
                  return Response(response)
            else:
               response =  ResponseData(module,"Departamento no encontrado",serializer.errors,status.HTTP_200_OK)  
               return Response(response)
         except Exception as ex:      
          response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
          return Response(responseData,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
       
class CiudadViewSet(viewsets.ModelViewSet):
   queryset = CiudadModel.objects.all()        
   serializer_class = CiudadSerializer
   model = CiudadModel 
   def create(self, request, format=None):
      module= "CiudadViewSet/create"
      try:
         serializer= CiudadSerializer(data = request.data,context={'request': request})
         if serializer.is_valid():
            serializer.save()
            response = ResponseData(module,"Ciudad creada exitosamente",serializer.data,status.HTTP_201_CREATED)
            return Response(response, status.HTTP_201_CREATED)
         else:
           response = ResponseData(module,"Ciudad no pudo ser creada",serializer.errors,status.HTTP_200_OK)  
           return Response(response, status=status.HTTP_200_OK)
        
      except Exception as ex:
         response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
         return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
   def partial_update(self,request,*args,**kwargs):
      if request.method == 'PATCH':
         module = "CiudadViewSet/partial_update"
         try:
            ciudad = CiudadModel.objects.filter(id = kwargs['pk']).exists()
            if ciudad :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = CiudadSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  with transaction.atomic():
                     serializer.save()
                     response =  ResponseData(module,"Ciudad actualizada",serializer.data,status.HTTP_201_CREATED)  
               else:
                   response =  ResponseData(module,"Ciudad no actualizada",serializer.errors,status.HTTP_200_OK)  
            else:
               response =  ResponseData(module,"Ciudad no encontrada",serializer.errors,status.HTTP_200_OK)  
            return Response(response)
         except Exception as ex:
            response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
            return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
   def update(self,request,*args,**kwargs):
      if request.method == 'PUT':
         module = "CiudadViewSet/update"
         try:
            ciudad = CiudadModel.objects.filter(id = kwargs['pk']).exists()
            if ciudad :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = CiudadSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  responseData = None
                  with transaction.atomic():
                     response =  ResponseData(module,"Ciudad actualizada",serializer.data,status.HTTP_201_CREATED)  
                  return Response(response)
               else:
                  response =  ResponseData(module,"Ciudad no actualizada",serializer.errors,status.HTTP_200_OK)  
                  return Response(response)
            else:
               response =  ResponseData(module,"Ciudad no encontrada",serializer.errors,status.HTTP_200_OK)  
               return Response(response)
         except Exception as ex:      
          response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
          return Response(responseData,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
class configuracionViewSet(viewsets.ModelViewSet):
   queryset = ConfiguracionModel.objects.all()        
   serializer_class = ConfiguracionSerializer
   model = ConfiguracionModel 
   def create(self, request, format=None):
      module= "configuracionViewSet/create"
      try:
         serializer= ConfiguracionSerializer(data = request.data,context={'request': request})
         if serializer.is_valid():
            serializer.save()
            response = ResponseData(module,"Configuracion creada exitosamente",serializer.data,status.HTTP_201_CREATED)
            return Response(response, status.HTTP_201_CREATED)
         else:
           response = ResponseData(module,"Configuracion no pudo ser creada",serializer.errors,status.HTTP_200_OK)  
           return Response(response, status=status.HTTP_200_OK)
        
      except Exception as ex:
         response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
         return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
   def partial_update(self,request,*args,**kwargs):
      if request.method == 'PATCH':
         module = "configuracionViewSet/partial_update"
         try:
            configuracion = ConfiguracionModel.objects.filter(id = kwargs['pk']).exists()
            if configuracion :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = ConfiguracionSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  with transaction.atomic():
                     serializer.save()
                     response =  ResponseData(module,"Configuracion actualizada",serializer.data,status.HTTP_201_CREATED)  
               else:
                   response =  ResponseData(module,"Configuracion no actualizada",serializer.errors,status.HTTP_200_OK)  
            else:
               response =  ResponseData(module,"Configuracion no encontrada",serializer.errors,status.HTTP_200_OK)  
            return Response(response)
         except Exception as ex:
            response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
            return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
   def update(self,request,*args,**kwargs):
      if request.method == 'PUT':
         module = "Configuracion/update"
         try:
            configuracion = ConfiguracionModel.objects.filter(id = kwargs['pk']).exists()
            if configuracion :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = ConfiguracionSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  responseData = None
                  with transaction.atomic():
                     response =  ResponseData(module,"Configuracion actualizada",serializer.data,status.HTTP_201_CREATED)  
                  return Response(response)
               else:
                  response =  ResponseData(module,"Configuracion no actualizada",serializer.errors,status.HTTP_200_OK)  
                  return Response(response)
            else:
               response =  ResponseData(module,"Configuracion no encontrada",serializer.errors,status.HTTP_200_OK)  
               return Response(response)
         except Exception as ex:      
          response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
          return Response(responseData,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
       
class LogViewSet(viewsets.ModelViewSet):
   queryset = LogModel.objects.all()        
   serializer_class = LogSerializer
   model = LogModel 
   

class EstadoUsuarioViewSet(viewsets.ModelViewSet):
   queryset = EstadoUsuarioModel.objects.all()        
   serializer_class = EstadoUsuarioSerializer
   model = EstadoUsuarioModel 
   def create(self, request, format=None):
      module= "EstadoUsuarioViewSet/create"
      try:
         serializer= EstadoUsuarioSerializer(data = request.data,context={'request': request})
         if serializer.is_valid():
            serializer.save()
            response = ResponseData(module,"Estado usuario creado exitosamente",serializer.data,status.HTTP_201_CREATED)
            return Response(response, status.HTTP_201_CREATED)
         else:
           response = ResponseData(module,"Estado usuario no pudo ser creado",serializer.errors,status.HTTP_200_OK)  
           return Response(response, status=status.HTTP_200_OK)
        
      except Exception as ex:
         response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
         return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
   def partial_update(self,request,*args,**kwargs):
      if request.method == 'PATCH':
         module = "EstadoUsuarioViewSet/partial_update"
         try:
            estado = EstadoUsuarioModel.objects.filter(id = kwargs['pk']).exists()
            if estado :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = EstadoUsuarioSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  with transaction.atomic():
                     serializer.save()
                     response =  ResponseData(module,"Estado usuario actualizado exitosamente",serializer.data,status.HTTP_201_CREATED)  
               else:
                   response =  ResponseData(module,"Estado usuario no pudo ser actualizado",serializer.errors,status.HTTP_200_OK)  
            else:
               response =  ResponseData(module,"Estado usuario no encontrado",serializer.errors,status.HTTP_200_OK)  
            return Response(response)
         except Exception as ex:
            response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
            return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
   def update(self,request,*args,**kwargs):
      if request.method == 'PUT':
         module = "EstadoUsuarioViewSet/update"
         try:
            estado = EstadoUsuarioModel.objects.filter(id = kwargs['pk']).exists()
            if estado :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = EstadoUsuarioSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  responseData = None
                  with transaction.atomic():
                     response =  ResponseData(module,"Configuracion actualizada",serializer.data,status.HTTP_201_CREATED)  
                  return Response(response)
               else:
                  response =  ResponseData(module,"Configuracion no actualizada",serializer.errors,status.HTTP_200_OK)  
                  return Response(response)
            else:
               response =  ResponseData(module,"Configuracion no encontrado",serializer.errors,status.HTTP_200_OK)  
               return Response(response)
         except Exception as ex:      
          response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
          return Response(responseData,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
       

class GeneroModelViewSet(viewsets.ModelViewSet):
   queryset = GeneroModel.objects.all()        
   serializer_class = GeneroSerializer
   model = GeneroModel
   def create(self, request, format=None):
      module= "GeneroModelViewSet/create"
      try:
         serializer= GeneroSerializer(data = request.data,context={'request': request})
         if serializer.is_valid():
            serializer.save()
            response = ResponseData(module,"Genero creado exitosamente",serializer.data,status.HTTP_201_CREATED)
            return Response(response, status.HTTP_201_CREATED)
         else:
           response = ResponseData(module,"Genero no pudo ser creado",serializer.errors,status.HTTP_200_OK)  
           return Response(response, status=status.HTTP_200_OK)
        
      except Exception as ex:
         response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
         return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
   def partial_update(self,request,*args,**kwargs):
      if request.method == 'PATCH':
         module = "GeneroModelViewSet/partial_update"
         try:
            genero = GeneroModel.objects.filter(id = kwargs['pk']).exists()
            if genero :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = GeneroSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  with transaction.atomic():
                     serializer.save()
                     response =  ResponseData(module,"Genero actualizado exitosamente",serializer.data,status.HTTP_201_CREATED)  
               else:
                   response =  ResponseData(module,"Genero no pudo ser actualizado",serializer.errors,status.HTTP_200_OK)  
            else:
               response =  ResponseData(module,"Genero no encontrado",serializer.errors,status.HTTP_200_OK)  
            return Response(response)
         except Exception as ex:
            response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
            return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   
   def update(self,request,*args,**kwargs):
      if request.method == 'PUT':
         module = "GeneroModelViewSet/update"
         try:
            genero = GeneroModel.objects.filter(id = kwargs['pk']).exists()
            if genero :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = GeneroSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  responseData = None
                  with transaction.atomic():
                     response =  ResponseData(module,"Genero  actualizado",serializer.data,status.HTTP_201_CREATED)  
                  return Response(response)
               else:
                  response =  ResponseData(module,"Genero no actualizado",serializer.errors,status.HTTP_200_OK)  
                  return Response(response)
            else:
               response =  ResponseData(module,"Genero no encontrado",serializer.errors,status.HTTP_200_OK)  
               return Response(response)
         except Exception as ex:      
          response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
          return Response(responseData,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     
       
       
class TipoDocumentoViewSet(viewsets.ModelViewSet):
   queryset = TipoDocumentoModel.objects.all()        
   serializer_class = TipoDocumentoSerializer
   model = TipoDocumentoModel 
   def create(self, request, format=None):
      module= "TipoDocumentoViewSet/create"
      try:
         serializer= TipoDocumentoSerializer(data = request.data,context={'request': request})
         if serializer.is_valid():
            serializer.save()
            response = ResponseData(module,"Tipo documento creado exitosamente",serializer.data,status.HTTP_201_CREATED)
            return Response(response, status.HTTP_201_CREATED)
         else:
           response = ResponseData(module,"Tipo documento no pudo ser creado",serializer.errors,status.HTTP_200_OK)  
           return Response(response, status=status.HTTP_200_OK)
        
      except Exception as ex:
         response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
         return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   
   def partial_update(self,request,*args,**kwargs):
      if request.method == 'PATCH':
         module = "TipoDocumentoViewSet/partial_update"
         try:
            tipo = TipoDocumentoModel.objects.filter(id = kwargs['pk']).exists()
            if tipo :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = TipoDocumentoSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  with transaction.atomic():
                     serializer.save()
                     response =  ResponseData(module,"Tipo documento actualizado exitosamente",serializer.data,status.HTTP_201_CREATED)  
               else:
                   response =  ResponseData(module,"Tipo documento no pudo ser actualizado",serializer.errors,status.HTTP_200_OK)  
            else:
               response =  ResponseData(module,"Tipo documento  no encontrado",serializer.errors,status.HTTP_200_OK)  
            return Response(response)
         except Exception as ex:
            response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
            return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
           
   def update(self,request,*args,**kwargs):
      if request.method == 'PUT':
         module = "TipoDocumentoViewSet/update"
         try:
            tipo = TipoDocumentoModel.objects.filter(id = kwargs['pk']).exists()
            if tipo :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = TipoDocumentoSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  responseData = None
                  with transaction.atomic():
                     response =  ResponseData(module,"Tipo documento  actualizado",serializer.data,status.HTTP_201_CREATED)  
                  return Response(response)
               else:
                  response =  ResponseData(module,"Tipo documento  no actualizado",serializer.errors,status.HTTP_200_OK)  
                  return Response(response)
            else:
               response =  ResponseData(module,"Tipo documento no encontrado",serializer.errors,status.HTTP_200_OK)  
               return Response(response)
         except Exception as ex:      
          response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
          return Response(responseData,status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class TipoUsuarioViewSet(viewsets.ModelViewSet):
   queryset = TipoUsuarioModel.objects.all()        
   serializer_class = TipoDocumentoSerializer
   model = TipoUsuarioModel 
   def create(self, request, format=None):
      module= "TipoUsuarioViewSet/create"
      try:
         serializer= TipoUsuarioSerializer(data = request.data,context={'request': request})
         if serializer.is_valid():
            serializer.save()
            response = ResponseData(module,"Tipo usuario creado exitosamente",serializer.data,status.HTTP_201_CREATED)
            return Response(response, status.HTTP_201_CREATED)
         else:
           response = ResponseData(module,"Tipo usuario no pudo ser creado",serializer.errors,status.HTTP_200_OK)  
           return Response(response, status=status.HTTP_200_OK)
        
      except Exception as ex:
         response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
         return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
   def partial_update(self,request,*args,**kwargs):
      if request.method == 'PATCH':
         module = "TipoUsuarioViewSet/partial_update"
         try:
            tipo = TipoUsuarioModel.objects.filter(id = kwargs['pk']).exists()
            if tipo :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = TipoDocumentoSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  with transaction.atomic():
                     serializer.save()
                     response =  ResponseData(module,"Tipo usuario actualizado exitosamente",serializer.data,status.HTTP_201_CREATED)  
               else:
                   response =  ResponseData(module,"Tipo usuario no pudo ser actualizado",serializer.errors,status.HTTP_200_OK)  
            else:
               response =  ResponseData(module,"Tipo usuario  no encontrado",serializer.errors,status.HTTP_200_OK)  
            return Response(response)
         except Exception as ex:
            response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
            return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
   def update(self,request,*args,**kwargs):
      if request.method == 'PUT':
         module = "TipoUsuarioViewSet/update"
         try:
            tipo = TipoUsuarioModel.objects.filter(id = kwargs['pk']).exists()
            if tipo :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = TipoUsuarioModel(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  responseData = None
                  with transaction.atomic():
                     response =  ResponseData(module,"Tipo usuario actualizado",serializer.data,status.HTTP_201_CREATED)  
                  return Response(response)
               else:
                  response =  ResponseData(module,"Tipo usuario no actualizado",serializer.errors,status.HTTP_200_OK)  
                  return Response(response)
            else:
               response =  ResponseData(module,"Tipo usuario no encontrado",serializer.errors,status.HTTP_200_OK)  
               return Response(response)
         except Exception as ex:      
          response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
          return Response(responseData,status=status.HTTP_500_INTERNAL_SERVER_ERROR)