from django.db import models

class Employee(models.Model):
    email = models.EmailField(max_length=10)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    employee_id = models.IntegerField()


    def __str__(self):
        return self.first_name


