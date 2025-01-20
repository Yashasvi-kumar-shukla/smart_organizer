from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('add/', views.add_task, name='add_task'),
    path('display/', views.display_tasks, name='display_tasks'),
    path('mark/', views.mark_complete, name='mark_complete'),
    path('', views.profile, name='profile'),
]