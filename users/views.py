from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(f'New user has been created with username {username} ')
            return HttpResponseRedirect('/')
    else:
        form=RegisterForm()
        return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    pq=User.objects.all()
    return render(request,'users/profile.html',{'pq':pq})

def acc_del(request,acc):
    f1=User.objects.get(id=acc).delete()
    return HttpResponseRedirect("/")