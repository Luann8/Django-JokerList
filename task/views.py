# task/views.py
from django.shortcuts import render, redirect, get_object_or_404
from task.models import Task
from django.utils import timezone


def edit_joke(request, pk):
    joke = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        joke.text = request.POST.get("task", "")
        joke.date = timezone.now()
        joke.edited = True
        joke.save()
        return redirect('/')

    context = {'joke': joke}
    return render(request, 'task/edit_joke.html', context)

