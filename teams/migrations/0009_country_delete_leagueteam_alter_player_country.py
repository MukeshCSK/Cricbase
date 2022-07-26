# Generated by Django 4.0.3 on 2022-06-01 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_rename_leagueteams_leagueteam_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='LeagueTeam',
        ),
        migrations.AlterField(
            model_name='player',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.country'),
        ),
    ]
