from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

from .models import Course, Book, Maruza

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'rating', 'created_at')
    search_fields = ('title', 'instructor')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating')
    search_fields = ('title', 'author')

@admin.register(Maruza)
class MaruzaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating')
    search_fields = ('title', 'author')