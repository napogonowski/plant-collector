# Generated by Django 4.2.4 on 2023-08-14 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feeding',
            old_name='meal',
            new_name='feed',
        ),
    ]