from django.db import models


# Create your models here
class Department(models.Model):
    dept_name = models.CharField(max_length=250)

    def __str__(self):
        return self.dept_name


class Course(models.Model):
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=250)

   #def __str__(self):
       #return self.course_name


class User(models.Model):
    #user_id=models.ForeignKey(auth_user,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField(blank=False)
    dob = models.DateTimeField()
    age = models.IntegerField()
    phone_num = models.IntegerField()
    address = models.TextField(max_length=250)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
