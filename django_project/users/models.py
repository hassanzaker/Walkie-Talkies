from django.db import models
from django.contrib.auth.models import User

class Type(models.TextChoices):
    Student = 'student'
    Teacher = 'teacher'
    admin = 'admin'


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    type = models.CharField(max_length=100, choices=Type.choices, default="student")

    # def __str__(self):
    #     return f'{self.user.username} Profile'
