from cmath import exp
from urllib import response
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from multiprocessing import context
from rest_framework import status

# Importaciones de modelo
from primerComponente.models import PrimerTabla

# importaciones de serializadores 
from primerComponente.serializers import PrimerTablaSerializers

# Create your views here.
class PrimerTablaList(APIView):
    def get(self, request, format=None):
        queryset = PrimerTabla.objects.all()
        serializers = PrimerTablaSerializers(queryset, many=True, context={'request': request})
        return Response(serializers.data)
        
    def post(self, request, format=None):
        serializer = PrimerTablaSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrimerTablaDetail(APIView):
    def get_objet(self, pk):
        try: 
            return PrimerTabla.objects.get(pk = pk)
        except PrimerTabla.DoesNotExist:
            return 0

    def get(self, request, pk, format=None):
        idResponse = self.get_objet(pk)
        if idResponse != 0:
            idResponse = PrimerTablaSerializers(idResponse)
            return Response(idResponse.data, status= status.HTTP_200_OK)
        return Response("No hay datos", status= status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        idResponse = self.get_objet(pk)
        serializer = PrimerTablaSerializers(idResponse, data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
