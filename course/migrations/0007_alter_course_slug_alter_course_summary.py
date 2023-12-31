# Generated by Django 4.0.8 on 2023-11-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_courseoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
