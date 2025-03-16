from django.db import models
from .student import Student
from .schedule import Schedule



class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True, blank=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True, blank=True)
    enroll_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'schedule'], name='unique_enrollment')
        ]

    def __str__(self):
        return f"{self.student} enrolled on { self.schedule}"




