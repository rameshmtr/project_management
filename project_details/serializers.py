from rest_framework import serializers
from .models import ProjectManagement, TaskManagement

class ProjectManagementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProjectManagement
        fields = ['id','name', 'description', 'duration', 'image']

class TaskManagementSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskManagement
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'project','user']


    
