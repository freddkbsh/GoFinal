from django.db import models

#create your models here
class Member(models.Model):
    fullname=models.CharField(max_length=100)
    email= models.EmailField()
    age= models.IntegerField()
    gender= models.CharField(max_length=50)
    yob= models.DateField()
    def __str__(self):
        return self.fullname

class product(models.Model):
    name= models.CharField(max_length=100)
    price= models.CharField(max_length=50)
    quantity= models.IntegerField()

    def __str__(self):
        return self.name


class Appointment1(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    phone= models.CharField(max_length=50)
    datetime= models.DateTimeField()
    department= models.CharField(max_length=50)
    doctor= models.CharField(max_length=50)
    message= models.TextField()

    def __str__(self):
        return self.name

class Contact1(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField()
    subject= models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name





