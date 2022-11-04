from rest_framework.response import Response
from django.shortcuts import render
from app.registro_votante.models import *
from rest_framework import viewsets,status
from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from app.registro_votante.serializer import *
from app.config.response import *

# Create your views here.
class RegistroVotanteViewSet(viewsets.ModelViewSet):
  queryset = RegistroVotanteModel.objects.all()        
  serializer_class = RegistroVotanteSerializer
  model = RegistroVotanteModel 
  def create(self, request, format=None):
      module= "RegistroVotanteViewSet/create"
      try:
         serializer= RegistroVotanteSerializer(data = request.data,context={'request': request})
         if serializer.is_valid():
            serializer.save()
            response = ResponseData(module,"Registro de votante creado exitosamente",serializer.data,status.HTTP_201_CREATED)
            return Response(response, status.HTTP_201_CREATED)
         else:
           response = ResponseData(module,"Registro de votante no creado",serializer.errors,status.HTTP_200_OK)  
           return Response(response, status=status.HTTP_200_OK)
      except Exception as ex:
         response = ResponseData(module,'Excepcion controlada: ' +str(ex) ,serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
         return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
  def partial_update(self,request,*args,**kwargs):       
     if request.method == 'PATCH':
         module = "RegistroVotanteViewSet/partial_update"
         try:
            registro = RegistroVotanteModel.objects.filter(id = kwargs['pk']).exists()
            if registro :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = RegistroVotanteSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  with transaction.atomic():
                     serializer.save()
                     response =  ResponseData(module,"Registro de votante actualizado correctamente",serializer.data,status.HTTP_201_CREATED)  
               else:
                   response =  ResponseData(module,"Registro de votante no pudo ser actualizado",serializer.errors,status.HTTP_200_OK)  
            else:
               response =  ResponseData(module,"Registro de votante no encontrado",serializer.errors,status.HTTP_200_OK)  
            return Response(response)
         except Exception as ex:
            response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
            return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   
  def update(self,request,*args,**kwargs):
      if request.method == 'PUT':
         module = "PuestoVotacionViewSet/update"
         try:
            registro = RegistroVotanteModel.objects.filter(id = kwargs['pk']).exists()
            if registro :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = RegistroVotanteSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  responseData = None
                  with transaction.atomic():
                     response =  ResponseData(module,"Registro de votante actualizado correctamente",serializer.data,status.HTTP_201_CREATED)  
                  return Response(response)
               else:
                  response =  ResponseData(module,"Registro de votante no pudo ser actualizado",serializer.errors,status.HTTP_200_OK)  
                  return Response(response)
            else:
               response =  ResponseData(module,"Registro de votante no encontrado",serializer.errors,status.HTTP_200_OK)  
               return Response(response)
         except Exception as ex:      
          response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
          return Response(responseData,status=status.HTTP_500_INTERNAL_SERVER_ERROR)