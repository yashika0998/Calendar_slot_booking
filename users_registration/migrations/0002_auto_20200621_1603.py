# Generated by Django 2.2.8 on 2020-06-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../media/../default.jpg', upload_to='profile_pics'),
        ),
    ]
