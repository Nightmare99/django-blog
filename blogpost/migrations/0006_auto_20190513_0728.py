# Generated by Django 2.2.1 on 2019-05-13 07:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0005_auto_20190513_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 13, 7, 28, 42, 2288, tzinfo=utc), verbose_name='Date of upload'),
        ),
    ]
