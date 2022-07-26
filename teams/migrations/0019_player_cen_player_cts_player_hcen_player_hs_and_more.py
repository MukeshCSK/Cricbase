# Generated by Django 4.0.4 on 2022-06-04 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0018_player_img_player_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='cen',
            field=models.CharField(default='', max_length=300, null=True, verbose_name='Cen'),
        ),
        migrations.AddField(
            model_name='player',
            name='cts',
            field=models.CharField(default='', max_length=300, null=True, verbose_name='Cts'),
        ),
        migrations.AddField(
            model_name='player',
            name='hcen',
            field=models.CharField(default='', max_length=300, null=True, verbose_name='Hcen'),
        ),
        migrations.AddField(
            model_name='player',
            name='hs',
            field=models.CharField(default='', max_length=300, null=True, verbose_name='Hs'),
        ),
        migrations.AddField(
            model_name='player',
            name='mat',
            field=models.CharField(default='', max_length=300, null=True, verbose_name='Mat'),
        ),
        migrations.AddField(
            model_name='player',
            name='runs',
            field=models.CharField(default='', max_length=300, null=True, verbose_name='runs'),
        ),
        migrations.AddField(
            model_name='player',
            name='wick',
            field=models.CharField(default='', max_length=300, null=True, verbose_name='Wick'),
        ),
    ]
