from django.contrib import admin
from .models import ProjectManagement, TaskManagement

# Register your models here.
admin.site.register(ProjectManagement)
admin.site.register(TaskManagement)
