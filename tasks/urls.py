from django.urls import path
from . import views

app_name = 'tasks'


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('<slug:slug>/', views.task_detail, name='task_detail'),
]
