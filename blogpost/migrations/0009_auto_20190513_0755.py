# Generated by Django 2.2.1 on 2019-05-13 07:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0008_auto_20190513_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 13, 7, 55, 22, 133400, tzinfo=utc), verbose_name='Date of upload'),
        ),
    ]