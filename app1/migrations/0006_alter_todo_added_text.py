# Generated by Django 3.2 on 2021-08-17 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_todo_added_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_text',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 17, 14, 9, 35, 694831)),
        ),
    ]
