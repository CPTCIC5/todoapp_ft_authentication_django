from django.shortcuts import render
from .models import Contact, Todo
from django.utils import timezone
from django.http import HttpResponseRedirect

def index(request):
    todo_item=Todo.objects.all().order_by("added_text")
    return render(request,'app1/index.html',{'todo_item':todo_item})

def add_todo(request):
    current_time=timezone.now()
    data=request.POST.get('text')
    todo=Todo.objects.create(added_text=current_time,text=data)
    return HttpResponseRedirect("/")

def delete_todo(request,question_id):
    delete=Todo.objects.get(id=question_id).delete()
    return HttpResponseRedirect("/")


def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        entry=Contact(name=name,email=email,phone=phone,message=message)
        entry.save()
    return render(request,'app1/contact.html')