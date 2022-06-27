from asyncio import tasks
from django.shortcuts import render

# Create your views here.
from .models import Task

from .serializers import Task, TaskSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


class TaskList(APIView):
    """ view all task"""

    def get(self,request, format=None):

        tasks =Task.objects.all()
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data)
        
