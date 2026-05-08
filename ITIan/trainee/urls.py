from django.urls import path
from . import views

urlpatterns=[
    path('list/', views.traineeList),
    path('<int:id>', views.viewTrainee, name="viewTrainee"),
    path('add/', views.addTrainee),
    path('update/<id>/', views.updateTrainee),
    path('delete/<id>/', views.deleteTrainee),
]