from django.shortcuts import render, redirect
from .models import task
from .forms import TaskForm
# Create your views here.
def index(request):
    tasks = task.objects.all()
    forms = TaskForm()
    if request.method == 'POST':
        forms = TaskForm(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('/')
    context = {'tasks': tasks, 'forms': forms}
    return render(request, 'todo/index.html', context)

def update_task(request, pk):
    tasks = task.objects.get(id=pk)
    forms = TaskForm(instance=tasks)
    if request.method == 'POST':
        forms = TaskForm(request.POST, instance=tasks)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    context = {'forms': forms}
    return render(request, 'todo/update_task.html', context)

def delete_task(request, pk):
        if request.method == 'POST':
            pi = task.objects.get(id=pk)
            pi.delete()
            return redirect('/')