from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

class ClassCreationForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['lesson', 'grade', 'class_num', "description"]

class ExamCreationForm(ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'description', 'exam_file']
