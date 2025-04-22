from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

class CustomLogoutView(auth_views.LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('course/', views.course_list, name='course'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('malumot/', views.malumot, name='malumot'),
    path('mycourse/', views.mycourse, name='mycourse'),
    path('add-to-my-courses/<int:pk>/', views.add_to_my_courses, name='add_to_my_courses'),
    path('books/', views.books, name='books'),
    path('detail/', views.detail, name='detail'),
    path('sertifikat/', views.sertifikat, name='sertifikat'),
    path('feature', views.feature, name='feature'),
    path('team', views.team, name='team'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('logout/', views.logout_view, name='logout'),
]