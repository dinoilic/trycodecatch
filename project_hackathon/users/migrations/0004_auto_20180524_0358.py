# Generated by Django 2.0.3 on 2018-05-24 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180524_0146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': {'User'}, 'verbose_name_plural': {'Users'}},
        ),
        migrations.AlterField(
            model_name='user',
            name='comment',
            field=models.TextField(max_length=500, null=True, verbose_name='Additional information such as gift-giving questionnaires blood'),
        ),
    ]
