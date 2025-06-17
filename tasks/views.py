from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
from .forms import TaskForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def task_list(request):
    tasks_list = Task.objects.all().order_by('-created_at')
    
    page = request.GET.get('page', 1)
    paginator = Paginator(tasks_list, 1)
    tasks = paginator.get_page(page)
    
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    
    return render(request, 'tasks/list.html', {'tasks': tasks})


def task_detail(request, slug):
    task = get_object_or_404(Task, slug=slug)
    return render(request, 'tasks/task_detail.html', {'task': task})


def create_task(request):
    
    context = {}
    form = TaskForm(request.POST or None)
    context['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:task_list')
        context['errors'] = form.errors
    
    return render(request, 'tasks/create.html', context)
    
    