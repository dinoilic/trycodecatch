# Generated by Django 2.0.3 on 2018-05-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180524_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
