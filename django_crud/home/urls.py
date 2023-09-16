from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('api/', views.apiOverview),
    path('task-list/', views.tasklist),
    path('task-detail/<str:pk>/', views.taskdetail),
    path('task-create/', views.taskcreate),
    path('task-update/<str:pk>/', views.taskupdate),
    path('task-delete/<str:pk>/', views.taskdelete),
    
]