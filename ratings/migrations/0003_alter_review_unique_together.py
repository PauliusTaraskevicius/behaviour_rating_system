# Generated by Django 3.2 on 2021-07-08 06:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ratings', '0002_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('reviewed_by', 'date')},
        ),
    ]