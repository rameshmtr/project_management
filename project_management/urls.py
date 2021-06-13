from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import ProjectManagementList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectManagementList.as_view(), name='Homepage'),
    path('project/', include('project_details.urls')),
]

urlpatterns += staticfiles_urlpatterns()
