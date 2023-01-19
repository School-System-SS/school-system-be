from django.urls import path
from .views import getAll, getOne, createSupervisor, UpdateSupervisor, DeleteSupervisor

urlpatterns = [
    path('get-all/', getAll.as_view()),
    path('get-one/<int:pk>', getOne.as_view()),
    path('create/', createSupervisor.as_view()),
    path('update/<int:pk>', UpdateSupervisor.as_view()),
    path('delete/<int:pk>', DeleteSupervisor.as_view()),
]