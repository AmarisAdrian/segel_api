from rest_framework.response import Response
from django.shortcuts import render
from app.votante.models import *
from rest_framework import viewsets,status
from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from app.votante.serializer import *
from app.config.response import *

# Create your views here.
class VotanteViewSet(viewsets.ModelViewSet):
    queryset = VotanteModel.objects.all()        
    serializer_class = VotanteSerializer
    model = VotanteModel
    def create(self, request, format=None):    
        module= "VotanteViewSet/create"
        try:
            serializer= VotanteSerializer(data = request.data,context={'request': request})
            if serializer.is_valid():
                serializer.save()
                response = ResponseData(module,"Votante creado exitosamente",serializer.data,status.HTTP_201_CREATED)
                return Response(response, status.HTTP_201_CREATED)
            else:
                response = ResponseData(module,"Votante no pudo ser creado",serializer.errors,status.HTTP_200_OK)  
            return Response(response, status=status.HTTP_200_OK)
        except Exception as ex:
            response = ResponseData(module,'Excepcion controlada: ' +str(ex) ,serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 

    def partial_update(self,request,*args,**kwargs):       
        if request.method == 'PATCH':
            module = "VotanteViewSet/partial_update"
            try:
                votante = VotanteModel.objects.filter(id = kwargs['pk']).exists()
                if votante :
                    partial = kwargs.pop('partial', False)
                    instance = self.get_object()
                    serializer = VotanteSerializer(instance, data=request.data,context={'request': request},partial=partial)
                    if serializer.is_valid():
                        with transaction.atomic():
                            serializer.save()
                            response =  ResponseData(module,"Votante actualizado correctamente",serializer.data,status.HTTP_201_CREATED)  
                    else:
                        response =  ResponseData(module,"Votante no pudo ser actualizado",serializer.errors,status.HTTP_200_OK)  
                else:
                    response =  ResponseData(module,"Votante no encontrado",serializer.errors,status.HTTP_200_OK)  
                return Response(response)
            except Exception as ex:
                response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
                return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def update(self,request,*args,**kwargs):
      if request.method == 'PUT':
         module = "VotanteViewSet/update"
         try:
            registro = User.objects.filter(id = kwargs['pk']).exists()
            if registro :
               partial = kwargs.pop('partial', False)
               instance = self.get_object()
               serializer = VotanteSerializer(instance, data=request.data,context={'request': request},partial=partial)
               if serializer.is_valid():
                  responseData = None
                  with transaction.atomic():
                     response =  ResponseData(module,"Votante  actualizado correctamente",serializer.data,status.HTTP_201_CREATED)  
                  return Response(response)
               else:
                  response =  ResponseData(module,"Votante no pudo ser actualizado",serializer.errors,status.HTTP_200_OK)  
                  return Response(response)
            else:
               response =  ResponseData(module,"Votante no encontrado",serializer.errors,status.HTTP_200_OK)  
               return Response(response)
         except Exception as ex:      
          response = ResponseData(module,'Excepcion controlada: ' +str(ex),serializer.data,status.HTTP_500_INTERNAL_SERVER_ERROR)  
          return Response(responseData,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
