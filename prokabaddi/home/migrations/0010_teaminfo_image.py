# Generated by Django 3.2.9 on 2021-11-16 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_player_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaminfo',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
