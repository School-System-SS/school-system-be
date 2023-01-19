from django.urls import path
from .views import SignUpView, getAllUsers

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('get-all/', getAllUsers.as_view()),
]