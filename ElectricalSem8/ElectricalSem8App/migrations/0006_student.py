# Generated by Django 2.2.19 on 2021-02-27 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElectricalSem8App', '0005_auto_20210227_0314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Id', models.IntegerField(primary_key='True', serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Gmail', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Discipline', models.CharField(choices=[('power', 'POWER'), ('telecom', 'TELECOM')], default='telecom', max_length=100)),
            ],
        ),
    ]