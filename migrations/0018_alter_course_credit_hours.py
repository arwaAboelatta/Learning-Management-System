# Generated by Django 5.0.7 on 2024-07-23 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_course_credit_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='credit_hours',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
