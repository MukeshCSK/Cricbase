# Generated by Django 4.0.4 on 2022-06-23 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0050_player_model_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='News_pic',
            field=models.ImageField(default='', null=True, upload_to='chicks/', verbose_name='News_pic'),
        ),
    ]
