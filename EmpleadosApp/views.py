from django.shortcuts import render
from django.http import JsonResponse

### IMPORTACIONES PARA API
from EmpleadosApp.models import Empleado
from EmpleadosApp.serializers import EmpleadoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
## SOLO PARA CLASES
from rest_framework.views import APIView

# Create your views here.
def empleadoView(request):
    emp = {
        'id': 123456,
        'nombre': 'Juan Perez',
        'email': 'juan@perez.cl',
        'salario': 1000
    }
    return JsonResponse(emp)

def empleado2View(request):
    empleados = Empleado.objects.all() #Se obtienen todos los empleados de la DB
    data = {'empleados': list(empleados.values('nombre','apellido'))} #Se convierte la lista de empleados en un diccionario
    return JsonResponse(data) #Se retorna la respuesta en formato JSON

#CREACION DE API

# GET /empleadosAPI/ -> Obtiene todos los empleados
# POST /empleadosAPI/ -> Crea un nuevo empleado

# GET /empleadosAPI/1/ -> Obtiene el empleado con id=1
# PUT /empleadosAPI/1/ -> Actualiza el empleado con id=1
# DELETE /empleadosAPI/1/ -> Elimina el empleado con id=1

@api_view(['GET', 'POST'])
def empleados_list(request):
    if request.method == 'GET':
        empleados = Empleado.objects.all() # Obtiene todos los empleados de la DB
        serializer = EmpleadoSerializer(empleados, many=True) # Se serializan los empleados
        return Response(serializer.data) # Se retorna la respuesta en formato JSON
    
    elif request.method == 'POST':
        serializer = EmpleadoSerializer(data=request.data) # Se serializan los datos recibidos
        if serializer.is_valid(): # Se verifica si los datos son validos
            serializer.save() # Se guardan los datos en la DB
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Se retorna la respuesta en formato JSON
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Se retorna la respuesta en formato JSON

@api_view(['GET', 'PUT', 'DELETE'])
def empleado_detail(request, pk):
    try:
        empleado = Empleado.objects.get(pk=pk) # Se obtiene el empleado con id=pk
    except Empleado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EmpleadoSerializer(empleado) # Se serializa el empleado
        return Response(serializer.data) # Se retorna la respuesta en formato JSON
    
    if request.method == 'PUT':
        serializer = EmpleadoSerializer(empleado, data=request.data) # Compara los datos enviados con los datos del empleado de la db
        if serializer.is_valid(): # Se verifica si los datos son validos
            serializer.save() # Se guardan los datos en la DB
            return Response(serializer.data) # Se retorna la respuesta en formato JSON
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Se retorna la respuesta en formato JSON
    
    if request.method == 'DELETE':
        empleado.delete() # Se elimina el empleado de la DB
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Creación de la API - Clases

class EmpleadoList(APIView):
    
    def get(self, request):
        empleados = Empleado.objects.all() # Obtiene todos los empleados de la DB
        serializer = EmpleadoSerializer(empleados, many=True) # Se serializan los empleados
        return Response(serializer.data) # Se retorna la respuesta en formato JSON
    
    def post(self, request):
        serializer = EmpleadoSerializer(data=request.data) # Se serializan los datos recibidos
        if serializer.is_valid(): # Se verifica si los datos son validos
            serializer.save() # Se guardan los datos en la DB
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Se retorna la respuesta en formato JSON
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Se retorna la respuesta en formato JSON
    
class EmpleadoDetail(APIView):
    
    def get_object(self, pk):
        try:
            empleado = Empleado.objects.get(pk=pk) # Se obtiene el empleado con id=pk
        except Empleado.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        empleado = Empleado.objects.get(pk=pk)
        serializer = EmpleadoSerializer(empleado) # Se serializa el empleado
        return Response(serializer.data) # Se retorna la respuesta en formato JSON
    
    def put(self, request, pk):
        empleado = Empleado.objects.get(pk=pk)
        serializer = EmpleadoSerializer(empleado, data=request.data) # Compara los datos enviados con los datos del empleado de la db
        if serializer.is_valid(): # Se verifica si los datos son validos
            serializer.save() # Se guardan los datos en la DB
            return Response(serializer.data) # Se retorna la respuesta en formato JSON
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Se retorna la respuesta en formato JSON
    
    def delete(self, request, pk):
        empleado = Empleado.objects.get(pk=pk)
        empleado.delete() # Se elimina el empleado de la DB
        return Response(status=status.HTTP_204_NO_CONTENT)