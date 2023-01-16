from django.urls import path
from .views import SignUpView, getAllUsers

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('getUsers/', getAllUsers.as_view())
]