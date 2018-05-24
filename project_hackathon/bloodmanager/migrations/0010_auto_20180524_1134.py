# Generated by Django 2.0.3 on 2018-05-24 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodmanager', '0009_auto_20180524_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='location',
            name='longitude',
        ),
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='postal_code',
            field=models.IntegerField(null=True),
        ),
    ]
