# Generated by Django 5.0.7 on 2024-07-23 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_remove_enrollment_course_remove_wishlist_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='instructor',
        ),
    ]
