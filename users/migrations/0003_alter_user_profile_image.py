# Generated by Django 3.2 on 2022-04-22 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='profile_pics/profile.png', upload_to='profile_pics'),
        ),
    ]