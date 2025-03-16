# Generated by Django 5.0.7 on 2024-08-07 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_course_credit_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='course_photos/'),
        ),
    ]
