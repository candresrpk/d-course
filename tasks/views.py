from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
from .forms import TaskForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
# Create your views here.

def task_list(request):
    tasks_list = Task.objects.all().order_by('-created_at')
    
    page = request.GET.get('page', 1)
    paginator = Paginator(tasks_list, 1)
    tasks = paginator.get_page(page)
    
    # generic = ''
    # campos = ['title', 'description', 'completed']
    # for task in tasks:
    #     for campo in campos:
    #         generic += str('?' + campo + '=' + str(getattr(task, campo)))
        
    
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
        
        
    context = {
        'tasks': tasks,
        # 'generic': generic
    }
    
    return render(request, 'tasks/list.html', context)


def task_detail(request, slug):
    task = get_object_or_404(Task, slug=slug)
    return render(request, 'tasks/task_detail.html', {'task': task})


def create_task(request):
    
    context = {}
    form = TaskForm(request.POST or None)
    # sent = False
    context['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            
            # sending emails
            
            # post_url = request.build_absolute_uri(task.get_absolute_url())
            # subject = f'{task.user.username} has created a task'
            # message = f'{task.title} - {post_url}'
            # send_mail(subject, message, sender='W2D0V@example.com', recipient=['W2D0V@example.com'])
            # sent = True
            
            return redirect('tasks:task_list')
        context['errors'] = form.errors
    
    return render(request, 'tasks/create.html', context)
    
    