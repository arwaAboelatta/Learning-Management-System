# Generated by Django 5.0.7 on 2024-08-12 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_instructor_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='company',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='instructor',
            old_name='position',
            new_name='university',
        ),
    ]
