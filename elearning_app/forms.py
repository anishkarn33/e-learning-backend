from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Course, CustomUser, Feedback, File

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','photo','is_student','is_teacher']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['course', 'content']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['course', 'file']
