from django.contrib import admin
from django.urls import path, include
from .views import  (ProjectManagementDetail, ProjectManagementCreate,
                    TaskManagementList, TaskManagementDetail, TaskManagementCreate)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [

    path('create/', ProjectManagementCreate.as_view(), name='Project Create'),
    path('details/<int:pk>/', ProjectManagementDetail.as_view(), name='Project Details'),
    path('<int:project_pk>/task/', TaskManagementList.as_view(), name='All Tasks'),
    path('<int:project_pk>/task/create/', TaskManagementCreate.as_view(), name='Task Create'),
    path('<int:project_pk>/task/<int:pk>/', TaskManagementDetail.as_view(), name='Task Details'),
    
]

urlpatterns += staticfiles_urlpatterns()





