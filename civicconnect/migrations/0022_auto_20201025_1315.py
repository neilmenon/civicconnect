# Generated by Django 3.1.1 on 2020-10-25 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civicconnect', '0021_auto_20201025_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 25, 13, 15, 28, 768277)),
        ),
    ]
