from rest_framework import serializers
from .models import ProjectManagement, TaskManagement

class ProjectManagementSerializer(serializers.ModelSerializer):

    image_name =  serializers.SerializerMethodField()

    def get_image_name(self, instance):
        return instance.image

    class Meta:
        model = ProjectManagement
        fields = ['id','name', 'description', 'duration', 'image_name']

class TaskManagementSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskManagement
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'project','user']


    
