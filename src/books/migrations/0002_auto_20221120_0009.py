# Generated by Django 3.2.16 on 2022-11-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='company_publish',
        ),
        migrations.AddField(
            model_name='book',
            name='need_login',
            field=models.IntegerField(default=0),
        ),
    ]
