# Generated by Django 2.0.6 on 2018-06-19 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180619_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]