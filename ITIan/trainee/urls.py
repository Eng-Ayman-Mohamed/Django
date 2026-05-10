from django.urls import path
from . import views

urlpatterns=[
    path('list/', views.traineeList, name="trainees"),
    path('<int:id>', views.viewTrainee, name="viewTrainee"),
    path('add/', views.addTrainee, name="addTrainee"),
    path('addTrainee/', views.addNewTrainee, name="addNewTrainee"),
    path('update/<id>/', views.updateTrainee),
    path('delete/<int:id>/', views.deleteTrainee, name="deleteTrainee"),
]