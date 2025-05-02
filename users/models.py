from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    rating = models.FloatField()
    image = models.ImageField(upload_to='courses/')
    created_at = models.DateTimeField(auto_now_add=True)
    enrolled_users = models.ManyToManyField(User, related_name='my_courses', blank=True)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    rating = models.FloatField()
    image = models.ImageField(upload_to='books/')
    file = models.FileField(upload_to='books/files/')

    def __str__(self):
        return self.title


class Maruza(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    rating = models.FloatField()
    image = models.ImageField(upload_to='maruza/')
    file = models.FileField(upload_to='maruza/files/')

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    GENDER_CHOICES = [
        ('1', 'Erkak'),
        ('2', 'Ayol'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    
    REGION_CHOICES = [
        ('', 'Tanlang'),
        ('2', 'Andijon viloyati'),
        ('3', 'Buxoro viloyati'),
        ('12', 'Farg\'ona viloyati'),
        ('4', 'Jizzax viloyati'),
        ('7', 'Namangan viloyati'),
        ('6', 'Navoiy viloyati'),
        ('5', 'Qashqadaryo viloyati'),
        ('1', 'Qoraqalpog\'iston Respublikasi'),
        ('8', 'Samarqand viloyati'),
        ('10', 'Sirdaryo viloyati'),
        ('9', 'Surxondaryo viloyati'),
        ('14', 'Toshkent shahri'),
        ('11', 'Toshkent viloyati'),
        ('13', 'Xorazm viloyati'),
    ]
    region = models.CharField(max_length=2, choices=REGION_CHOICES, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"