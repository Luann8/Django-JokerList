# train/views.py
from django.shortcuts import render, redirect
from task.models import Task
from django.utils import timezone

def index(request):
    if request.method == 'GET':
        # Retrieve all tasks ordered by date
        jokes = Task.objects.all().order_by('date').reverse()
        context = {'jokes': jokes}
        return render(request, 'task/index.html', context)
    elif request.method == 'POST':
        action = request.POST.get("action", "")
        if action == "add":
            # Add new joke
            text = request.POST.get("task", "")
            new_joke = Task(text=text, date=timezone.now())
            new_joke.save()
        elif action == "delete":
            # Delete existing joke
            task_id = request.POST.get("task_id", "")
            Task.objects.filter(id=task_id).delete()

        return redirect('/')