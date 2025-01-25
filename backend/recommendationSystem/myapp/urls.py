from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/get_predictions/", views.get_model_predict, name="get_predictions"),
    path("todos/", views.todos, name="Todos"),
    path('api/todos/', views.todo_list, name='todo_list'),          # API: Lista elementów + dodawanie
    path('api/todos/<int:pk>/', views.todo_detail, name='todo_detail'), 
]