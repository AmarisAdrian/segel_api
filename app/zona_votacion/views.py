from rest_framework.response import Response
from django.shortcuts import render
from app.zona_votacion.models import *
from rest_framework import viewsets,status
from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from app.zona_votacion.serializer import *
from app.config.response import *


class ZonaVotacionViewSet(viewsets.ModelViewSet):
    queryset = ZonaVotacionModel.objects.all()        
    serializer_class = ZonaVotacionSerializer
    model = ZonaVotacionModel
    def create(self, request, format=None):    
        module= "ZonaVotacionViewSet/create"
        try:
            serializer= ZonaVotacionSerializer(data = request.data,context={'request': request})
            if serializer.is_valid():
                serializer.save()
                response = ResponseData(module,"Zona de votacion creada exitosamente",serializer.data,status.HTTP_201_CREATED)
                return Response(response, status.HTTP_201_CREATED)
            else:
                response = ResponseData(module,"Zona de votacion no pudo ser creado",serializer.errors,status.HTTP_200_OK)  
            return Response(response, status=status.HTTP_200_OK)
        except Exception as ex:
            response = ResponseData(module,'Excepcion controlada: ' +str(ex) ,serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def partial_update(self,request,*args,**kwargs):       
        if request.method == 'PATCH':
            module = "ZonaVotacionViewSet/partial_update"
            try:
                zona = ZonaVotacionModel.objects.filter(id = kwargs['pk']).exists()
                if zona :
                    partial = kwargs.pop('partial', False)
                    instance = self.get_object()
                    serializer = ZonaVotacionSerializer(instance, data=request.data,context={'request': request},partial=partial)
                    if serializer.is_valid():
                        with transaction.atomic():
                            serializer.save()
                            response =  ResponseData(module,"Zona de votacion actualizada correctamente",serializer.data,status.HTTP_201_CREATED)  
                    else:
                        response =  ResponseData(module,"Zona de votacion no pudo ser actualizada",serializer.errors,status.HTTP_200_OK)  
                else:
                    response =  ResponseData(module,"Zona de votacion no encontrada",serializer.errors,status.HTTP_200_OK)  
                return Response(response)
            except Exception as ex:
                response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
                return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def update(self,request,*args,**kwargs):
      if request.method == 'PUT':
         module = "ZonaVotacionViewSet/update"
         try:
            registro = ZonaVotacionModel.objects.filter(id = kwargs['pk']).exists()
            if registro :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = ZonaVotacionSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  responseData = None
                  with transaction.atomic():
                     response =  ResponseData(module,"Zona de votación actualizada correctamente",serializer.data,status.HTTP_201_CREATED)  
                  return Response(response)
               else:
                  response =  ResponseData(module,"Zona de votación no pudo ser actualizada",serializer.errors,status.HTTP_200_OK)  
                  return Response(response)
            else:
               response =  ResponseData(module,"Zona de votación no encontrada",serializer.errors,status.HTTP_200_OK)  
               return Response(response)
         except Exception as ex:      
          response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
          return Response(responseData,status=status.HTTP_500_INTERNAL_SERVER_ERROR)