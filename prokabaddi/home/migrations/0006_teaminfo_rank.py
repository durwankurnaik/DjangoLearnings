# Generated by Django 3.2.9 on 2021-11-14 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211114_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaminfo',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
