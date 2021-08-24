from django.db import models
from django.contrib.auth.models import AbstractUser

# # Create your models here.
class User(AbstractUser):
    mobile = models.BigIntegerField(default=0)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Quiz(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE, blank=True, null=True)
    createdon = models.DateField(default='')

class Questions(models.Model):
    question = models.CharField(max_length=3000)
    option1 = models.CharField(max_length=1500)
    option2 = models.CharField(max_length=1500)
    option3 = models.CharField(max_length=1500)
    option4 = models.CharField(max_length=1500)
    answer = models.CharField(max_length=1500)
    relatedquiz = models.ForeignKey(Quiz, related_name='quiz', on_delete=models.CASCADE)

class Answer(models.Model):
    quiz = models.ForeignKey(Quiz,related_name="ansquiz", on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, related_name="questions", on_delete=models.CASCADE)
    answer = models.CharField(max_length=1500)
    correct = models.BooleanField(default=False)
    student = models.ForeignKey(User,related_name="student",on_delete=models.CASCADE)