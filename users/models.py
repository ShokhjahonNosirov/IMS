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
