# Generated by Django 4.1.3 on 2022-11-23 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='descrption',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]