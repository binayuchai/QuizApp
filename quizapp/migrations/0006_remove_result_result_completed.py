# Generated by Django 4.1.5 on 2023-01-19 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0005_rename_is_completed_result_result_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='result_completed',
        ),
    ]