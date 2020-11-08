from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post, Classroom
from .backend.backend import *

def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


@login_required
def dashboard(request):
    # for now we assume the user is of type student and show his classes
    return render(request, 'blog/dashboard.html', {'classrooms': request.user.classrooms_as_student.all()})


def classroom(request):
    # todo: recover classroom object from the request
    classroom = None
    return render(request, 'blog/classroom.html', {'forums': get_forums(classroom), 'exams': get_exams(classroom)})


def forum(request):
    # todo: recover forum object from the request
    forum = None
    return render(request, 'blog/forum.html', {'posts': get_posts(forum)})


def exam(request):
    # todo: recover exam object from the request
    exam = None
    return render(request, 'blog/exam.html', {'exam': exam})