from rest_framework.response import Response
from django.shortcuts import render
from app.anexo.models import *
from rest_framework import viewsets,status
from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from app.puesto_votacion.serializer import *
from app.config.response import *

class PuestoVotacionViewSet(viewsets.ModelViewSet):
   queryset = PuestoVotacionModel.objects.all()        
   serializer_class = PuestoVotacionSerializer
   model = PuestoVotacionModel 
   def create(self, request, format=None):
      module= "PuestoVotacionViewSet/create"
      try:
         serializer= PuestoVotacionSerializer(data = request.data,context={'request': request})
         if serializer.is_valid():
            serializer.save()
            response = ResponseData(module,"Puesto votacion creado exitosamente",serializer.data,status.HTTP_201_CREATED)
            return Response(response, status.HTTP_201_CREATED)
         else:
           response = ResponseData(module,"Puesto votacion no pudo ser creado",serializer.errors,status.HTTP_200_OK)  
           return Response(response, status=status.HTTP_200_OK)
      except Exception as ex:
         response = ResponseData(module,'Excepcion controlada: ' +str(ex) ,serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
         return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
   def partial_update(self,request,*args,**kwargs):     
    if request.method == 'PATCH':
        module = "PuestoVotacionViewSet/partial_update"
        try:
           puesto = PuestoVotacionModel.objects.filter(id = kwargs['pk']).exists()
           if puesto :
              partial = kwargs.pop('partial', False)
              instance = self.get_object()
              serializer = PuestoVotacionSerializer(instance, data=request.data,context={'request': request},partial=partial)
              if serializer.is_valid():
                 with transaction.atomic():
                    serializer.save()
                    response =  ResponseData(module,"Puesto votación actualizado correctamente",serializer.data,status.HTTP_201_CREATED)  
              else:
                  response =  ResponseData(module,"Puesto de votación no pudo ser actualizado",serializer.errors,status.HTTP_200_OK)  
           else:
              response =  ResponseData(module,"Puesto de votacion no encontrado",serializer.errors,status.HTTP_200_OK)  
           return Response(response)
        except Exception as ex:
           response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
           return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
   
   def update(self,request,*args,**kwargs):
      if request.method == 'PUT':
         module = "PuestoVotacionViewSet/update"
         try:
            puesto = PuestoVotacionModel.objects.filter(id = kwargs['pk']).exists()
            if puesto :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = PuestoVotacionSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  responseData = None
                  with transaction.atomic():
                     response =  ResponseData(module,"Puesto de votacion actualizado correctamente",serializer.data,status.HTTP_201_CREATED)  
                  return Response(response)
               else:
                  response =  ResponseData(module,"Puesto de votacion no pudo ser actualizado",serializer.errors,status.HTTP_200_OK)  
                  return Response(response)
            else:
               response =  ResponseData(module,"Puesto de votacion no encontrado",serializer.errors,status.HTTP_200_OK)  
               return Response(response)
         except Exception as ex:      
          response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
          return Response(responseData,status=status.HTTP_500_INTERNAL_SERVER_ERROR)