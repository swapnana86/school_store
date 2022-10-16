from django.db import models


# Create your models here
class Department(models.Model):
    dept_name = models.CharField(max_length=250)


class Course(models.Model):
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=250)


class User(models.Model):
    username = models.CharField(max_length=250, blank=False)
    password = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    email = models.EmailField(blank=False)
    dob = models.DateTimeField()
    age = models.IntegerField()
    phone_num = models.IntegerField()
    address = models.TextField(max_length=250)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
