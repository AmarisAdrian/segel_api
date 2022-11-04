from rest_framework.response import Response
from django.shortcuts import render
from app.divipol.models import *
from rest_framework import viewsets,status
from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from app.divipol.serializer import *
from app.config.response import *

# Create your views here.
class DivipolViewSet(viewsets.ModelViewSet):
   queryset = DivipolModel.objects.all()        
   serializer_class = DivipolSerializer
   model = DivipolModel 
   def create(self, request, format=None):
      module= "DivipolViewSet/create"
      try:
         serializer= DivipolSerializer(data = request.data,context={'request': request})
         if serializer.is_valid():
            serializer.save()
            response = ResponseData(module,"Divipol creada exitosamente",serializer.data,status.HTTP_201_CREATED)
            return Response(response, status.HTTP_201_CREATED)
         else:
           response = ResponseData(module,"Divipol no pudo ser creado",serializer.errors,status.HTTP_200_OK)  
           return Response(response, status=status.HTTP_200_OK)
      except Exception as ex:
         response = ResponseData(module,'Excepcion controlada: ' +str(ex) ,serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
         return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
   def partial_update(self,request,*args,**kwargs):     
    if request.method == 'PATCH':
        module = "DivipolViewSet/partial_update"
        try:
           divipol = DivipolModel.objects.filter(id = kwargs['pk']).exists()
           if divipol :
              partial = kwargs.pop('partial', False)
              instance = self.get_object()
              serializer = DivipolSerializer(instance, data=request.data,context={'request': request},partial=partial)
              if serializer.is_valid():
                 with transaction.atomic():
                    serializer.save()
                    response =  ResponseData(module,"Divipol actualizado correctamente",serializer.data,status.HTTP_201_CREATED)  
              else:
                  response =  ResponseData(module,"Divipol no pudo ser actualizado",serializer.errors,status.HTTP_200_OK)  
           else:
              response =  ResponseData(module,"Divipol no encontrada",serializer.errors,status.HTTP_200_OK)  
           return Response(response)
        except Exception as ex:
           response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
           return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
          
   def update(self,request,*args,**kwargs):
      if request.method == 'PUT':
         module = "DivipolViewSet/update"
         try:
            divipol = DivipolModel.objects.filter(id = kwargs['pk']).exists()
            if divipol :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = DivipolSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  responseData = None
                  with transaction.atomic():
                     response =  ResponseData(module,"Divipol actualizado",serializer.data,status.HTTP_201_CREATED)  
                  return Response(response)
               else:
                  response =  ResponseData(module,"Divipol no actualizado",serializer.errors,status.HTTP_200_OK)  
                  return Response(response)
            else:
               response =  ResponseData(module,"Divipol no encontrado",serializer.errors,status.HTTP_200_OK)  
               return Response(response)
         except Exception as ex:      
          response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
          return Response(responseData,status=status.HTTP_500_INTERNAL_SERVER_ERROR)