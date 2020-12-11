from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('update-task/<int:pk>/', views.update_task, name="update"),
    path('delete-task/<int:pk>/', views.delete_task, name="delete")
]
