from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    salary=models.FloatField()
    email=models.CharField(max_length=35)

#many to many -----------------------------------------
class Programmer(models.Model):
    name = models.CharField(max_length=20)
    sal = models.IntegerField()

class Project(models.Model):
    name = models.CharField(max_length=30)
    progrmmers = models.ManyToManyField(Programmer)
#-------------------------------------------------------

#Many to One -------------------------------------------
class Customer(models.Model):
    name = models.CharField(max_length=20)

class PhoneNumber(models.Model):
    type = models.CharField(max_length=20)
    number = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)#on delete function for deleteing phone number when customer get deleted.
#--------------------------------------------------------

#One to One ---------------------------------------------
class Person(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=10)
    age = models.IntegerField()

class License(models.Model):
    type= models.CharField(max_length=10)
    validFrom=models.DateField()
    validTo=models.DateField()
    person = models.OneToOneField(Person,on_delete=models.CASCADE)