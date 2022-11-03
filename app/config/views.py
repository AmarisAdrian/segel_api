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
   model = DepartamentoSerializer 
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
         response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
         return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

   def partial_update(self,request,*args,**kwargs):
      if request.method == 'PATCH':
         module = "EditDepartamento"
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
         module = "UpdateDepartamento"
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