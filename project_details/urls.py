from django.contrib import admin
from django.urls import path, include
from .views import  (ProjectManagementDetail, ProjectManagementCreate, ProjectUpdateView, ProjectDelete,
                    TaskManagementList, TaskManagementDetail, TaskManagementCreate, TaskUpdateview,TaskDelete)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [

    path('create/', ProjectManagementCreate.as_view(), name='Project Create'),
    path('details/<int:pk>/', ProjectManagementDetail.as_view(), name='Project Details'),
    path('details/update/<int:pk>/', ProjectUpdateView.as_view(), name='Project Update'),
    path('details/delete/<int:pk>/', ProjectDelete.as_view(), name='Project Delete'),
    path('<int:project_pk>/task/', TaskManagementList.as_view(), name='All Tasks'),
    path('<int:project_pk>/task/create/', TaskManagementCreate.as_view(), name='Task Create'),
    path('<int:project_pk>/task/<int:pk>/', TaskManagementDetail.as_view(), name='Task Details'),
    path('<int:project_pk>/task/<int:pk>/', TaskManagementDetail.as_view(), name='Task Details'),
    path('<int:project_pk>/task/update/<int:pk>/', TaskUpdateview.as_view(), name='Task Update'),
    path('<int:project_pk>/task/delete/<int:pk>/', TaskDelete.as_view(), name='TaskDelete'),
    
]

urlpatterns += staticfiles_urlpatterns()





