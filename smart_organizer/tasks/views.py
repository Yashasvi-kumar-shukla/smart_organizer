from django.shortcuts import render,redirect
from django.utils.timezone import now
from .models import Task

# Create your views here.


def display_tasks(request):
    tasks = Task.objects.filter(is_complete=False)  # Only fetch tasks for the logged-in user
    return render(request, 'tasks/display_tasks.html', {
        'tasks': tasks,
        'current_time':now(),
    })

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        deadline = request.POST['deadline']
        priority = request.POST['priority']
        Task.objects.create(title=title, deadline=deadline, priority=priority)
        return redirect('profile')  # Redirect to home after adding task
    return render(request, 'tasks/add_task.html')

def mark_complete(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids')
        Task.objects.filter(id__in=task_ids).update(is_complete=True)
        return redirect('profile')  # Redirect to home after marking complete
    tasks = Task.objects.filter(is_complete=False)
    return render(request, 'tasks/mark_complete.html', {'tasks': tasks})

def profile(request):
    return render(request, 'tasks/profile.html')