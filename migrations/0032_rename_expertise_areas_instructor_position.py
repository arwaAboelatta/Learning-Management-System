# Generated by Django 5.0.7 on 2024-08-12 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_instructor_biography_instructor_experience_years_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='expertise_areas',
            new_name='position',
        ),
    ]
