from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserAccount(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    userType = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=15)
    subject = models.CharField(max_length=255,default="student")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



class materials(models.Model):
    account = get_user_model()
    author = models.ForeignKey(account,on_delete=models.CASCADE)
    materials = models.FileField(null=True)
    title = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    time_added = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=255,null=True)

    def __str__(self): 
        return self.title

class Profile(models.Model):
    account = get_user_model()
    user = models.OneToOneField(account, on_delete=models.CASCADE)
    ProfilePic = models.ImageField(default='../static/externalFiles/images/crs1.jpg',upload_to="profilePics/")
    bio = models.TextField()

    def __str__(self):
        return self.user.firstname

class Questions(models.Model):
    account = get_user_model()
    student = models.ForeignKey(account,on_delete=models.CASCADE)
    studentProfile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    question = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.studentProfile.user.firstname


class Answers(models.Model):
    account = get_user_model()
    author = models.ForeignKey(account,on_delete=models.CASCADE)
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    authorProfile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    answer = models.TextField(null=True)
    rating = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.authorProfile.user.firstname






