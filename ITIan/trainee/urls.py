from django.urls import path
from . import views

urlpatterns=[
    path('list/', views.traineeList.as_view(), name="trainees"),
    path('<int:id>', views.viewTrainee, name="viewTrainee"),
    path('add/', views.addTrainee.as_view(), name="addTrainee"),
    path('addTrainee/', views.addNewTrainee.as_view(), name="addNewTrainee"),
    path('update/<id>/', views.updateTrainee),
    path('delete/<int:id>/', views.deleteTrainee, name="deleteTrainee"),
]