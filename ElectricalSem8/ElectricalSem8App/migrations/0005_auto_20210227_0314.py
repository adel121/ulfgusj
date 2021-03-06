# Generated by Django 2.2.19 on 2021-02-27 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElectricalSem8App', '0004_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='Discipline',
            field=models.CharField(choices=[('power', 'POWER'), ('telecom', 'TELECOM'), ('common', 'COMMON')], default='telecom', max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='Content',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
