# Generated by Django 4.0.8 on 2023-11-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0005_alter_result_id_alter_takencourse_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='level',
            field=models.CharField(choices=[('Bachlor', 'Bachlor Degree'), ('Master', 'Master Degree')], max_length=25, null=True),
        ),
    ]
