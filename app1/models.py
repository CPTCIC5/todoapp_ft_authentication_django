from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Todo(models.Model):
    added_text=models.DateTimeField()
    text=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.text

    class Meta():
        verbose_name_plural='Todo"s'
        ordering=['-text']

class Contact(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(default='xyz@gmail.com')
    phone=models.CharField(max_length=50,null=True)
    message=models.TextField(null=True)

    def __str__(self):
        return self.email
