# Generated by Django 3.1 on 2021-07-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0005_auto_20210706_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz_model',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='quiz_model',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]