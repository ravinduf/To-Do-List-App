from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import TaskForm
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'tasks/list.html',{'tasks':tasks,'form':form})

def updateTask(request,pk):
    pk=get_object_or_404(Task,pk=pk)

    form = TaskForm(instance=pk)

    if request.method == "POST":
        form =TaskForm(request.POST,instance=pk)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'tasks/update_task.html',{'form':form})