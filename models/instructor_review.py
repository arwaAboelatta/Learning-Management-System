from django.db import models
from django.contrib.auth.models import User
from . import Instructor

class InstructorReview(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='course_reviews')
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'instructor')

    def __str__(self):
        return f'Review by {self.student.username} for {self.instructor.first_name}'