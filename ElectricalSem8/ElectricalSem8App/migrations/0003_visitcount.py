# Generated by Django 2.2.19 on 2021-02-26 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElectricalSem8App', '0002_course_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Count', models.IntegerField(default=0)),
            ],
        ),
    ]
