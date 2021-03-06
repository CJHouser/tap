# Generated by Django 3.1.3 on 2021-01-24 00:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210123_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='modified_date',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 24, 0, 21, 7, 947173, tzinfo=utc), editable=False),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 24, 0, 21, 7, 947173, tzinfo=utc), editable=False),
        ),
    ]
