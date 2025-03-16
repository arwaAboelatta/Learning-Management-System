from django.db import models
from .instructor import Instructor

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=200)
    credit_hours = models.IntegerField(default=2)
    instructors = models.ManyToManyField(Instructor)
    photo = models.ImageField(upload_to='course_photos/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    topics_covered = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.course_name
