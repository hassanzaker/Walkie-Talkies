from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import Profile
from .backend.backend import *
from .forms import *
from django.views.decorators.http import condition



def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


@login_required()
def dashboard(request):
    # for now we assume the user is of type student and show his classes
    if Profile.objects.get(user_id= request.user).type == 'teacher':
        return render(request, 'blog/dashboard.html', {'classrooms': request.user.classrooms_as_teacher.all(),
                                                       'type': Profile.objects.get(user_id=request.user).type})
    elif Profile.objects.get(user_id= request.user).type == 'student' or True:
        return render(request, 'blog/dashboard.html', {'classrooms': request.user.classrooms_as_student.all(),
                                                   'type': Profile.objects.get(user_id= request.user).type})


@login_required()
def classroom(request, classroom_id):
    if match(user=request.user, classroom_id=classroom_id):
        classroom = Classroom.objects.get(id=classroom_id)
        return render(request, 'blog/classroom.html', {'forums': get_forums(classroom), 'exams': get_exams(classroom)})
    else:
        messages.error(request, 'Sorry, We found out that you are not a member of the classroom!')
        return redirect('dashboard')

@login_required()
def create_classroom(request):
    if request.method == 'POST':
        form = ClassCreationForm(request.POST)
        if form.is_valid():
            form =form.save()
            form.teacher = Profile.objects.get(user_id= request.user).user
            form.save()
            messages.success(request, f'Class has been created!')
            return redirect('dashboard') # except dashboard it should redirect to class's page
    else:
        form = ClassCreationForm()
    if Profile.objects.get(user_id= request.user).type == 'teacher':
        return render(request, 'blog/create_classroom.html', {'form': form})
    else:
        return render(request, 'blog/404.html', {})


@login_required()
def join_classroom(request):
    if Profile.objects.get(user_id= request.user).type == 'student':
        return render(request, 'blog/join_classroom.html', {})
    else:
        return render(request, 'blog/404.html', {})



@login_required()
def forum(request, classroom_id, forum_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        create_post(content, request.user, forum_id)

    if match(user=request.user, classroom_id=classroom_id, forum_id=forum_id):
        forum = get_forums(Classroom.objects.get(id=classroom_id)).get(id=forum_id)
        return render(request, 'blog/forum.html', {'posts': get_posts(forum)})
    else:
        messages.error(request, 'Something went wrong!')
        return redirect('dashboard')


def exam(request):
    # todo: recover exam object from the request
    exam = None
    return render(request, 'blog/exam.html', {'exam': exam})