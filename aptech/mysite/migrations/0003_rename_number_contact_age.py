# Generated by Django 5.0.7 on 2024-08-21 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_alter_contact_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='number',
            new_name='age',
        ),
    ]
