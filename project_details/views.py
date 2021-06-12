# -------------------Model imports-------------------------
from .models import ProjectManagement, TaskManagement
from django.contrib.auth.models import User

# -------------------Serializer imports--------------------
from .serializers import ProjectManagementSerializer, TaskManagementSerializer

# -------------------restframework imports-----------------
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

# -------------------Template imports----------------------
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect

# from rest_framework.permissions import AllowAny


class ProjectManagementCreate(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'projectform.html'

    def get(self, request):
        profile = get_object_or_404(ProjectManagement, pk=1)
        serializer = ProjectManagementSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request):

        instance = ProjectManagement.objects.create(name = request.data.get('name'),
                                                    description = request.data.get('description'),
                                                    duration = request.data.get('duration'),
                                                    image = request.data.get('image'))
        instance .save()
        return redirect('Project Create')

class ProjectManagementDetail(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'project_detail.html'

    def get_object(self, pk):
        try:
            return ProjectManagement.objects.get(pk=pk)
        except ProjectManagement.DoesNotExist:
            raise Http404

    def get(self, request, pk):

        queryset = self.get_object(pk)

        return Response({'projects': queryset})

    
    def put(self, request,pk):

        instance = self.get_object(pk)

        if request.data.get('name'):
            instance.name = request.data.get('name')

        if request.data.get('description'):
            instance.description = request.data.get('description')

        if request.data.get('duration'):
            instance.duration = request.data.get('duration')

        if request.data.get('image'):
            instance.image = request.data.get('image')

        instance.save()

        return Response(ProjectManagementSerializer(instance).data)


    def delete(self, request,pk):

        instance = self.get_object(pk)
        instance.delete()

        return Response(status=200)


class TaskManagementList(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'task_details.html'

    def get(self, request, project_pk,format=None):

        project_queryset = ProjectManagement.objects.get(id = project_pk)

        queryset = TaskManagement.objects.filter(project=project_pk)
        serializer = TaskManagementSerializer(queryset, many=True)

        return Response({'tasks': queryset, 'project':project_queryset})

class TaskManagementCreate(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'task_form.html'

    def get(self, request, project_pk):
        profile = get_object_or_404(TaskManagement, pk=1)
        serializer = TaskManagementSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, project_pk):
        instance = TaskManagement.objects.create(name = request.data.get('name'),
                                                description = request.data.get('description'),
                                                start_date = request.data.get('start_date'),
                                                end_date = request.data.get('end_date'),
                                                project = ProjectManagement.objects.get(id = project_pk),
                                                user = User.objects.get(id = 1))

        instance.save()

        return Response({'messages':'Created Successfully'})

class TaskManagementDetail(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'task_info.html'

    def get_object(self, pk, project_pk):
        try:
            return TaskManagement.objects.get(pk=pk)
        except TaskManagement.DoesNotExist:
            raise Http404

    def get(self, request, pk, project_pk):

        project_queryset = ProjectManagement.objects.get(id = project_pk)

        queryset = self.get_object(pk, project_pk)
        serializer = TaskManagementSerializer(queryset)

        return Response({'task': queryset, 'project':project_queryset})

        
    
    def put(self, request,pk):
        print('this')

        instance = self.get_object(pk)

        if request.data.get('name'):
            instance.name = request.data.get('name')

        if request.data.get('description'):
            instance.description = request.data.get('description')

        if request.data.get('start_date'):
            instance.start_date = request.data.get('start_date')
        
        if request.data.get('end_date'):
            instance.end_date = request.data.get('end_date')

        if request.data.get('project'):
            instance.project = ProjectManagement.objects.get(id = request.data.get('project_management'))

        if request.data.get('user_id'):
            instance.user_id = User.objects.get(id = request.data.get('user_id'))

        instance.save()

        return Response(TaskManagementSerializer(instance).data)


    def delete(self, request,pk):

        instance = self.get_object(pk)
        instance.delete()

        return Response(status=200)

