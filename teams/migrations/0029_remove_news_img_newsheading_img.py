# Generated by Django 4.0.3 on 2022-06-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0028_newsheading_news_alter_newsheading_newsheading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='Img',
        ),
        migrations.AddField(
            model_name='newsheading',
            name='img',
            field=models.ImageField(default='', null=True, upload_to='images/'),
        ),
    ]
