# Generated by Django 4.2.4 on 2023-08-22 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_courses_price_alter_courses_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='price',
            field=models.IntegerField(default='25000'),
        ),
    ]