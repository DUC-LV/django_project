# Generated by Django 3.2.16 on 2022-11-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('author', models.CharField(max_length=100)),
                ('company_publish', models.CharField(max_length=200)),
                ('type_book', models.CharField(max_length=200)),
                ('snippet', models.TextField()),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]