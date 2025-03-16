from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=11)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
       return self.first_name + self.last_name

    def is_in_wishlist(self, course):
        return self.wishlist_set.filter(course=course).exists()

