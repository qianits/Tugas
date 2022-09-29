import imp
from multiprocessing import context
from urllib import response
from django.shortcuts import render
from todolist.models import Task, User
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import Input_Form


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    var = request.COOKIES.get('last_login', 'UserNotFound')
    if var == "UserNotFound":
        response = HttpResponseRedirect(reverse("todolist:login"))
        return response
    data_todolist = Task.objects.filter(user=request.user)
    context = {
    'username' : request.user.username,
    'data' : data_todolist,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = Input_Form(request.POST)
    if (form.is_valid() and request.method == 'POST'):
        Task.objects.create(title=form.cleaned_data["title"], description=form.cleaned_data["description"], date=datetime.datetime.now(), user=request.user)
        return redirect('todolist:show_todolist')
    form = Input_Form()
    context = {"form":form}
    return render(request, "create-task.html", context=context)

@login_required(login_url='/todolist/login/')
def remove(request, id):
    Task.objects.get(id=id).delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def status(request, id):
    todo = Task.objects.get(id=id)
    todo.is_finished = not(todo.is_finished)
    todo.save()
    return redirect('todolist:show_todolist')
