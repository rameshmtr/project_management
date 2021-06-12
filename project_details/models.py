from django.db import models
from django.db.models import fields
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import User

# Create your models here.

class ProjectManagement(models.Model):

    name = fields.CharField(max_length=128, blank=True, null=True)
    description = fields.TextField(blank=True, null=True)
    duration = fields.CharField(max_length=128, blank=True, null = True)
    image = models.ImageField(upload_to = 'assets/', null=True)

class TaskManagement(models.Model):

    name = fields.CharField(max_length=128, blank=True, null=True)
    description = fields.TextField(blank=True, null=True)
    start_date = fields.DateField(blank=True, null=True)
    end_date = fields.DateField(blank=True, null=True)
    project = models.ForeignKey(ProjectManagement, on_delete=PROTECT)
    user = models.ForeignKey(User, on_delete=PROTECT)