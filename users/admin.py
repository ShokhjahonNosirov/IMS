from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'rating', 'created_at')
    search_fields = ('title', 'instructor')