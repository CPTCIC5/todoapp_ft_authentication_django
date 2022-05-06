from django.shortcuts import render,get_object_or_404
from .models import Contact, Todo
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime

def index(request):
    todo_item=Todo.objects.all().order_by("added_text")
    return render(request,'app1/index.html',{'todo_item':todo_item})


@login_required
def add_todo(request):
    if request.method == 'POST':
        current_time=timezone.now()
        data=request.POST.get('text')
        todo=Todo.objects.create(added_text=current_time,text=data,author=request.user)
        return HttpResponseRedirect(reverse('app1:index'))
    return HttpResponseRedirect("/")

@login_required
def edit_todo(request,text):
    #queryset=Todo.objects.get(text=text)
    queryset=get_object_or_404(Todo,text=text)
    if request.user == queryset.author:
        if request.method == 'POST':
            text=request.POST.get('text')
            #print(queryset,len(text))
            """
                        if len(text)>2 and len(text)>200:
                messages.success(request,'text must be from 2 to 200 chars')
                return HttpResponseRedirect(reverse('app1:edit_todo'),args=[queryset.text])
            """
            queryset.text=text
            queryset.added_text=datetime.datetime.now()
            queryset.save()
            messages.success(request,'Updated')
            return HttpResponseRedirect(reverse('app1:index'))
    else:
        messages.success(request,'u can"t edit someone else post')
        return HttpResponseRedirect(reverse('app1:index'))
    return render(request,'app1/edit.html')

@login_required
def delete_todo(request,question_id):
    #delete=Todo.objects.get(id=question_id)
    delete=get_object_or_404(Todo,id=question_id)
    if delete.author == request.user:
        delete.delete()
    else:
        return HttpResponse("You can't cez u won't cez it's post of anyother user n it's a bad thing..")
    return HttpResponseRedirect("/")


def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        entry=Contact(name=name,email=email,phone=phone,message=message)
        entry.save()
        return HttpResponseRedirect(reverse('app1:contact'))
    return render(request,'app1/contact.html')