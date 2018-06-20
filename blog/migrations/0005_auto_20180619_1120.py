# Generated by Django 2.0.6 on 2018-06-19 11:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180619_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish_data',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
