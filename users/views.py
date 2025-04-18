# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegisterForm
from .models import Course

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or wherever you want
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def course(request):
    return render(request, 'course.html')

def detail(request):
    return render(request, 'detail.html')

def feature(request):
    return render(request, 'feature.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def course_list(request):
    query = request.GET.get('q', '')  # Default to an empty string if 'q' is not in the request
    if query:
        courses = Course.objects.filter(title__icontains=query)  # Filter courses by title
    else:
        courses = Course.objects.all()  # Show all courses if no query
    return render(request, 'course.html', {'courses': courses, 'query': query})


