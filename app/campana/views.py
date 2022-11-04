from rest_framework.response import Response
from django.shortcuts import render
from app.campana.models import *
from rest_framework import viewsets,status
from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from app.campana.serializer import *
from app.config.response import *
# Create your views here.
class CampanaViewSet(viewsets.ModelViewSet):
   queryset = CampanaModel.objects.all()        
   serializer_class = CampanaSerializer
   model = CampanaModel 
   def create(self, request, format=None):
      module= "CampanaViewSet/create"
      try:
         serializer= CampanaSerializer(data = request.data,context={'request': request})
         if serializer.is_valid():
            serializer.save()
            response = ResponseData(module,"Campana creada exitosamente",serializer.data,status.HTTP_201_CREATED)
            return Response(response, status.HTTP_201_CREATED)
         else:
           response = ResponseData(module,"Campana no pudo ser creado",serializer.errors,status.HTTP_200_OK)  
           return Response(response, status=status.HTTP_200_OK)
      except Exception as ex:
         response = ResponseData(module,'Excepcion controlada: ' +str(ex) ,serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
         return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     
   def partial_update(self,request,*args,**kwargs):     
    if request.method == 'PATCH':
        module = "CampanaViewSet/partial_update"
        try:
           campana = CampanaModel.objects.filter(id = kwargs['pk']).exists()
           if campana :
              partial = kwargs.pop('partial', False)
              instance = self.get_object()
              serializer = CampanaSerializer(instance, data=request.data,context={'request': request},partial=partial)
              if serializer.is_valid():
                 with transaction.atomic():
                    serializer.save()
                    response =  ResponseData(module,"Campaña actualizada correctamente",serializer.data,status.HTTP_201_CREATED)  
              else:
                  response =  ResponseData(module,"Campaña no pudo ser actualizada",serializer.errors,status.HTTP_200_OK)  
           else:
              response =  ResponseData(module,"Campaña no encontrada",serializer.errors,status.HTTP_200_OK)  
           return Response(response)
        except Exception as ex:
           response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
           return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
          
   def update(self,request,*args,**kwargs):
      if request.method == 'PUT':
         module = "CampanaViewSet/update"
         try:
            campana = CampanaModel.objects.filter(id = kwargs['pk']).exists()
            if campana :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = CampanaSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  responseData = None
                  with transaction.atomic():
                     response =  ResponseData(module,"Campaña actualizada",serializer.data,status.HTTP_201_CREATED)  
                  return Response(response)
               else:
                  response =  ResponseData(module,"Campaña no actualizada",serializer.errors,status.HTTP_200_OK)  
                  return Response(response)
            else:
               response =  ResponseData(module,"Campaña no encontrada",serializer.errors,status.HTTP_200_OK)  
               return Response(response)
         except Exception as ex:      
          response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
          return Response(responseData,status=status.HTTP_500_INTERNAL_SERVER_ERROR)