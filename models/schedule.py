from django.db import models
from .course import Course

class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET(None), null=True, blank=True)
    created_on = models.DateField()
    updated_date = models.DateField()

    def __str__(self):
        return f"{self.course} Schedule"
