# Generated by Django 2.0.6 on 2018-06-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180619_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='users_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]