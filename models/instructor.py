from django.contrib.auth.models import User
from django.db import models


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.SET(None), null=True, blank=True, unique=True)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=11)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.TextField(null=True, blank=True)
    qualifications = models.TextField(null=True, blank=True)
    experience_years = models.PositiveIntegerField(null=True, blank=True)
    university = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='instructors/', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name




