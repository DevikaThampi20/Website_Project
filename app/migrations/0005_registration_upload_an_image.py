# Generated by Django 4.2.4 on 2023-08-14 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_courses_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='upload_an_image',
            field=models.FileField(default='image.jpg', upload_to='documents'),
        ),
    ]
