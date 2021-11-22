# Generated by Django 3.2.9 on 2021-11-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_teaminfo_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopRaiders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]