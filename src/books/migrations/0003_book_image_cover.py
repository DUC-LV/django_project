# Generated by Django 3.2.8 on 2022-11-20 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20221120_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image_cover',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
