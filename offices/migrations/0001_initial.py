# Generated by Django 3.2 on 2021-04-22 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name_plural': 'offices',
            },
        ),
    ]
