# Generated by Django 3.1 on 2021-07-06 15:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_auto_20210706_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz_model',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='quiz_name',
            field=models.CharField(default=datetime.datetime(2021, 7, 6, 15, 52, 23, 738344, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz_model',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
