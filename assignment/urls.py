from django.urls import path
from .views import AssignmentDataView, AssignmentCertainDataView, AssignmentUpdateView, AssignmentDeleteView, AssignmentCreateView

urlpatterns = [
    path('', AssignmentDataView.as_view()),
    path('get/<int:pk>', AssignmentCertainDataView.as_view()),
    path('create/', AssignmentCreateView.as_view()),
    path('update/<int:pk>', AssignmentUpdateView.as_view()),
    path('delete/<int:pk>', AssignmentDeleteView.as_view()),

]

