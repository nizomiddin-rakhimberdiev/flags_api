# Generated by Django 5.1.3 on 2024-11-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flags',
            name='image',
            field=models.ImageField(upload_to='flags_image/'),
        ),
    ]
