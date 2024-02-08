from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-detail/<str:pk>/', views.taskDetails, name='task-detail'),
    path('task-create/', views.createTask, name='task-create'),
    path('task-update/<str:pk>/', views.updateTask, name='task-update'),
    path('task-delete/<str:pk>/', views.deleteTask, name='task-delete'),
]