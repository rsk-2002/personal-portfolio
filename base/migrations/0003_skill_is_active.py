# Generated by Django 4.0.1 on 2022-04-29 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_project_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
