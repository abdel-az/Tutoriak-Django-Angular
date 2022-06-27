
from rest_framework import serializers
from .models import Task

class TaskSecrializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','title', 'content', 'created_on',  'due_date')
