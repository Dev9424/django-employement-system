# Generated by Django 4.2.11 on 2024-03-16 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='last_name',
            new_name='location',
        ),
    ]
