# Generated by Django 4.0.3 on 2022-06-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0046_alter_news_created_alter_news_newsheading'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='summary',
            field=models.CharField(default='', max_length=300, null=True, verbose_name='summary'),
        ),
        migrations.AddField(
            model_name='news',
            name='tour',
            field=models.CharField(default='', max_length=300, null=True, verbose_name='tour'),
        ),
    ]
