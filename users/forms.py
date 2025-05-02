# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text=""
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=""  # Removed the default help text
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=""  # Removed the default help text
    )

    first_name = forms.CharField(max_length=100, label='Ism')
    last_name = forms.CharField(max_length=100, label='Familiya')
    middle_name = forms.CharField(max_length=100, label='Sharif', required=False)
    age = forms.IntegerField(label='Yoshingiz')
    GENDER_CHOICES = [
        ('male', 'Erkak'),
        ('female', 'Ayol'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Jinsingiz')
    REGION_CHOICES = [
        ('', 'Tanlang'),
        ('Toshkent sh', 'Toshkent sh'),
        ('Buxoro', 'Samarqand'),
        ('bukhara', 'Buxoro'),
        ('Andijon', 'Andijon'),
        ('Farg‘ona', 'Farg‘ona'),
        ('Namangan', 'Namangan'),
        ('Jizzax', 'Jizzax'),
        ('Navoiy', 'Navoiy'),
        ('Qashqadaryo', 'Qashqadaryo'),
        ('Qoraqalpog‘iston Respublikasi', 'Qoraqalpog‘iston Respublikasi'),
        ('Sirdaryo', 'Sirdaryo'),
        ('Surxondaryo', 'Surxondaryo'),
        ('Toshkent viloyati', 'Toshkent viloyati'),
        ('Xorazm', 'Xorazm'),
        # Add other regions
    ]
    region = forms.ChoiceField(choices=REGION_CHOICES, label='Viloyat')
    city = forms.CharField(max_length=100, label='Shahar yoki tuman')
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                  'middle_name', 'age', 'gender', 'region', 'city']