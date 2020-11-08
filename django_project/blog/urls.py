from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/classroom/<int:classroom_id>/', views.classroom, name='classroom'),
    path('dashboard/classroom/<int:classroom_id>/<int:forum_id>/', views.forum, name='forum'),

]
