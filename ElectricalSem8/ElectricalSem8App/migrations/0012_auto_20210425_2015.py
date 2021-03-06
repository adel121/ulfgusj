# Generated by Django 2.2.19 on 2021-04-25 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElectricalSem8App', '0011_auto_20210415_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewer',
            name='bio1',
            field=models.CharField(default='unchosen', max_length=200),
        ),
        migrations.AddField(
            model_name='viewer',
            name='biomate',
            field=models.CharField(default='unchosen', max_length=200),
        ),
        migrations.AddField(
            model_name='viewer',
            name='data1',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viewer',
            name='data2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viewer',
            name='data3',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viewer',
            name='data4',
            field=models.CharField(default='unchosen', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='viewer',
            name='datamate',
            field=models.CharField(default='unchosen', max_length=200),
        ),
    ]
