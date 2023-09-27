from django.db import models
import datetime
# Create your models here.

class contactus(models.Model):
    Name = models.CharField(max_length=100)
    Number = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Message = models.TextField()


class signup(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/profile/')
    email = models.CharField(max_length=100, primary_key=True)
    address = models.TextField()

class signup_reporter(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/profile_reporter/')
    email = models.CharField(max_length=100, primary_key=True)
    address = models.TextField()
    def __str__(self):
        return self.name


class feedbackus(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/feedback/')
    email = models.CharField(max_length=100)
    feedback = models.TextField()


class category(models.Model):
    name = models.CharField(max_length=40)
    Npic = models.ImageField(upload_to="static/category", null=True)
    def __str__(self):
        return self.name
    

class ourblog(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='static/blog/')
    Data = models.TextField()
    Date = models.DateField(("Date"), default=datetime.date.today)


class mynews(models.Model):
    newstitle = models.TextField()
    newsdec = models.TextField()
    newsimage = models.ImageField(upload_to='static/news/')
    newscategory = models.ForeignKey(category, on_delete=models.CASCADE)
    newsdate = models.DateField(("Date"), default=datetime.date.today)
    newsreporter = models.ForeignKey(signup_reporter, on_delete=models.CASCADE)
