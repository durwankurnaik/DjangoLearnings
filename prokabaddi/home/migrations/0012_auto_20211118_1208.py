# Generated by Django 3.2.9 on 2021-11-18 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20211117_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='city',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='user',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
