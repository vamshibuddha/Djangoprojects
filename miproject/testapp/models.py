from django.db import models


# Create your models here.
# Abstract base class model inheritance
class ContactInfo(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=264)

    class Meta:
        abstract = True


class Student(ContactInfo):
    rollno = models.IntegerField()
    marks = models.IntegerField()


class Teacher(ContactInfo):
    subject = models.CharField(max_length=128)
    salary = models.FloatField()


# Multi table inheritance
class ContactInfo01(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=264)


class Student01(ContactInfo01):
    rollno = models.IntegerField()
    marks = models.IntegerField()


class Teacher01(ContactInfo01):
    subject = models.CharField(max_length=128)
    salary = models.FloatField()


# Multiple inheritance
class Parent(models.Model):
    fd1 = models.CharField(max_length=128)
    fd2 = models.CharField(max_length=128)


class Child(Parent):
    fd3 = models.CharField(max_length=128)
    fd4 = models.CharField(max_length=128)


class SubChild(Child):
    fd5 = models.CharField(max_length=128)

