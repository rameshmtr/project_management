# Generated by Django 3.2.4 on 2021-06-11 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_details', '0003_taskmanagement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmanagement',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskmanagement',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
