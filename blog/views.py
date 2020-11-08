from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post, Classroom


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


@login_required
def dashboard(request):
    # for now we assume the user is of type student and show his classes
    return render(request, 'blog/dashboard.html', {'classrooms': request.user.classrooms_as_student.all()})
