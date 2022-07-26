# Generated by Django 4.0.4 on 2022-06-05 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0024_alter_player_playerimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, null=True, verbose_name='Venue Name')),
                ('address', models.CharField(default='', max_length=100, null=True, verbose_name='Address')),
                ('zip_code', models.CharField(default='', max_length=100, null=True, verbose_name='Zip')),
                ('phone', models.CharField(default='', max_length=100, null=True, verbose_name='Phone')),
                ('web', models.URLField(default='', null=True, verbose_name='Web Address')),
                ('email_address', models.EmailField(default='', max_length=254, null=True, verbose_name='Email Address')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, null=True, verbose_name='Event Name')),
                ('event_date', models.DateTimeField(default='', null=True, verbose_name='Event Date')),
                ('manager', models.CharField(default='', max_length=110, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.venue')),
            ],
        ),
    ]
