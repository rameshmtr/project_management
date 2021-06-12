from django.shortcuts import render
from django.http import HttpResponse
from project_details.models import ProjectManagement
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

# def homepage(request):
#     # return HttpResponse('HI')
#     return render(request, 'homepage.html')

class ProjectManagementList(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'homepage.html'

    def get(self, request, format=None):

        queryset = ProjectManagement.objects.all()

        return Response({'projects': queryset})
