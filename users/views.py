# users/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .forms import RegisterForm
from .models import Course, Book, Maruza, Profile  # Assuming you have a Profile model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Create profile for the new user
            profile = Profile(
                user=user,
                middle_name=form.cleaned_data.get('middle_name'),
                age=form.cleaned_data.get('age'),
                gender=form.cleaned_data.get('gender'),
                region=form.cleaned_data.get('region'),
                city=form.cleaned_data.get('city')
            )
            profile.save()
            
            return redirect('login')
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

@login_required
def malumot(request):
    # Get the user's profile or create if it doesn't exist
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # Update user info
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.save()
        
        # Update profile info
        profile.middle_name = request.POST.get('middle_name')
        profile.age = request.POST.get('age')
        profile.gender = request.POST.get('gender')
        profile.region = request.POST.get('region')
        profile.city = request.POST.get('city')
        profile.save()
        
        messages.success(request, "Ma'lumotlaringiz muvaffaqiyatli yangilandi!")
        return redirect('malumot')
    
    return render(request, 'malumot.html', {'profile': profile})

@login_required
def mycourse(request):
    my_courses = request.user.my_courses.all()  # Fetch courses added by the user
    return render(request, 'mycourse.html', {'my_courses': my_courses})

def books(request):
    query = request.GET.get('q', '').strip()  # Get the search query and strip extra spaces
    if query:
        books = Book.objects.filter(title__icontains=query)  # Filter books by title
        # print(f"Search Query: {query}, Results: {books}")  # Debugging
    else:
        books = Book.objects.all()  # Show all books if no query
    return render(request, 'books.html', {'books': books, 'query': query})

def sertifikat(request):
    return render(request, 'sertifikat.html')   

def detail(request):
    return render(request, 'detail.html')

def maruzalar(request):
    query = request.GET.get('q', '').strip()  # Get the search query and strip extra spaces
    if query:
        maruzalar = Maruza.objects.filter(title__icontains=query)  # Filter books by title
        # print(f"Search Query: {query}, Results: {books}")  # Debugging
    else:
        maruzalar = Maruza.objects.all()  # Show all books if no query
    return render(request, 'maruzalar.html', {'maruzalar': maruzalar, 'query': query})

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def course_list(request):
    query = request.GET.get('q', '').strip()  # Get the search query and strip extra spaces
    if query:
        courses = Course.objects.filter(title__icontains=query)  # Filter courses by title
        print(f"Search Query: {query}, Results: {courses}")  # Debugging
    else:
        courses = Course.objects.all()  # Show all courses if no query
    return render(request, 'course.html', {'courses': courses, 'query': query})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'detail.html', {'course': course})

@login_required
def add_to_my_courses(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.enrolled_users.add(request.user)  # Add the user to the course's enrolled users
    return redirect('course_detail', pk=pk)  # Redirect back to the course detail page


