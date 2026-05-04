from django.urls import path
from .import views

urlpatterns=[
    path('list/', views.courseList),
    path('add/', views.addCourse),
    path('update/<id>/', views.updateCourse),
    path('delete/<id>/', views.deleteCourse),
]