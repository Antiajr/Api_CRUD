from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
from .models import Task

# Create your views here.
@api_view(['GET'])
def apiOverview(resquest):
    api_urls = {
        'list': '/task-list',
        'detail-view': '/task-detail/<str:pk>/',
        'create': '/task-create/',
        'update': '/task-update/<str:pk>/',
        'delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetails(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializers(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializers(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def updateTask(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializers(instance=tasks, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def deleteTask(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()

    return Response("Item Successfull Deleted")    