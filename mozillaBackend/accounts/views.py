from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .form import registerForm
# Create your views here.
def indexView(request):
    return render(request,'index.html')

@login_required(login_url='/login/')
def dashboardView(request):
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = registerForm()
    return render(request,'registration/register.html',{'form':form})