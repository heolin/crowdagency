from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def list(request):
    """Display list of tasks"""
    return render(request, 'tasks/list.html', {})


@login_required
def view(request, task_id):
    """Main views of one task"""
    return render(request, 'tasks/task.html', {})

