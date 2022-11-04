from rest_framework.response import Response
from django.shortcuts import render
from app.anexo.models import *
from rest_framework import viewsets,status
from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from app.anexo.serializer import *
from app.config.response import *

class AnexoUsuarioViewSet(viewsets.ModelViewSet):
   queryset = AnexoUsuarioModel.objects.all()        
   serializer_class = AnexoUsuarioSerializer
   model = AnexoUsuarioModel 
   def create(self, request, format=None):
      module= "AnexoUsuarioViewSet/create"
      try:
         serializer= AnexoUsuarioSerializer(data = request.data,context={'request': request})
         if serializer.is_valid():
            serializer.save()
            response = ResponseData(module,"Anexo subido exitosamente",serializer.data,status.HTTP_201_CREATED)
            return Response(response, status.HTTP_201_CREATED)
         else:
           response = ResponseData(module,"Anexo no pudo ser subido ",serializer.errors,status.HTTP_200_OK)  
           return Response(response, status=status.HTTP_200_OK)
      except Exception as ex:
         response = ResponseData(module,'Excepcion controlada: ' +str(ex) ,serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
         return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   
   def partial_update(self,request,*args,**kwargs):     
    if request.method == 'PATCH':
        module = "AnexoUsuarioViewSet/partial_update"
        try:
           anexo = AnexoUsuarioModel.objects.filter(id = kwargs['pk']).exists()
           if anexo :
              partial = kwargs.pop('partial', False)
              instance = self.get_object()
              serializer = AnexoUsuarioSerializer(instance, data=request.data,context={'request': request},partial=partial)
              if serializer.is_valid():
                 with transaction.atomic():
                    serializer.save()
                    response =  ResponseData(module,"Anexo usuario actualizado correctamente",serializer.data,status.HTTP_201_CREATED)  
              else:
                  response =  ResponseData(module,"Anexo de usuario no pudo ser actualizado",serializer.errors,status.HTTP_200_OK)  
           else:
              response =  ResponseData(module,"Anexo no encontrado",serializer.errors,status.HTTP_200_OK)  
           return Response(response)
        except Exception as ex:
           response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
           return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
   def update(self,request,*args,**kwargs):
      if request.method == 'PUT':
         module = "CampanaViewSet/update"
         try:
            campana = AnexoUsuarioModel.objects.filter(id = kwargs['pk']).exists()
            if campana :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = AnexoUsuarioSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  responseData = None
                  with transaction.atomic():
                     response =  ResponseData(module,"Anexo usuario actualizo",serializer.data,status.HTTP_201_CREATED)  
                  return Response(response)
               else:
                  response =  ResponseData(module,"Anexo usuario no pudo ser actualizado",serializer.errors,status.HTTP_200_OK)  
                  return Response(response)
            else:
               response =  ResponseData(module,"Anexo no encontrado",serializer.errors,status.HTTP_200_OK)  
               return Response(response)
         except Exception as ex:      
          response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
          return Response(responseData,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
       
class AnexoVotanteViewSet(viewsets.ModelViewSet):
   queryset = AnexoVotanteModel.objects.all()        
   serializer_class = AnexoVotanteSerializer
   model = AnexoVotanteModel 
   def create(self, request, format=None):
      module= "AnexoVotanteViewSet/create"
      try:
         serializer= AnexoVotanteSerializer(data = request.data,context={'request': request})
         if serializer.is_valid():
            serializer.save()
            response = ResponseData(module,"Anexo subido exitosamente",serializer.data,status.HTTP_201_CREATED)
            return Response(response, status.HTTP_201_CREATED)
         else:
           response = ResponseData(module,"Anexo no pudo ser subido ",serializer.errors,status.HTTP_200_OK)  
           return Response(response, status=status.HTTP_200_OK)
      except Exception as ex:
         response = ResponseData(module,'Excepcion controlada: ' +str(ex) ,serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
         return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
   def partial_update(self,request,*args,**kwargs):     
    if request.method == 'PATCH':
        module = "AnexoVotanteViewSet/partial_update"
        try:
           anexo = AnexoVotanteModel.objects.filter(id = kwargs['pk']).exists()
           if anexo :
              partial = kwargs.pop('partial', False)
              instance = self.get_object()
              serializer = AnexoVotanteSerializer(instance, data=request.data,context={'request': request},partial=partial)
              if serializer.is_valid():
                 with transaction.atomic():
                    serializer.save()
                    response =  ResponseData(module,"Anexo votante actualizado correctamente",serializer.data,status.HTTP_201_CREATED)  
              else:
                  response =  ResponseData(module,"Anexo de votante no pudo ser actualizado",serializer.errors,status.HTTP_200_OK)  
           else:
              response =  ResponseData(module,"Anexo no encontrado",serializer.errors,status.HTTP_200_OK)  
           return Response(response)
        except Exception as ex:
           response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
           return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
   def update(self,request,*args,**kwargs):
      if request.method == 'PUT':
         module = "AnexoVotanteViewSet/update"
         try:
            campana = AnexoVotanteModel.objects.filter(id = kwargs['pk']).exists()
            if campana :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = AnexoVotanteSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  responseData = None
                  with transaction.atomic():
                     response =  ResponseData(module,"Anexo votante actualizo",serializer.data,status.HTTP_201_CREATED)  
                  return Response(response)
               else:
                  response =  ResponseData(module,"Anexo votante no pudo ser actualizado",serializer.errors,status.HTTP_200_OK)  
                  return Response(response)
            else:
               response =  ResponseData(module,"Anexo no encontrado",serializer.errors,status.HTTP_200_OK)  
               return Response(response)
         except Exception as ex:      
          response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
          return Response(responseData,status=status.HTTP_500_INTERNAL_SERVER_ERROR)