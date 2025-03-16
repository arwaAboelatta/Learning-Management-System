from django.db import models
from .course import Course
from .student import Student



class Wishlist(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    enroll_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.student.first_name}'s wishlist for {self.course.course_name}"



