# Generated by Django 4.0.3 on 2022-06-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0010_remove_seriesname_seriesteams_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news',
            field=models.TextField(),
        ),
    ]