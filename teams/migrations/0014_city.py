# Generated by Django 4.0.4 on 2022-06-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0013_news_newsheading'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
    ]
