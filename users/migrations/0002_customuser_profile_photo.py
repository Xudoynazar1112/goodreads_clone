# Generated by Django 5.0.4 on 2024-05-16 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_photo',
            field=models.ImageField(default='guest-user.jpg', upload_to=''),
        ),
    ]
