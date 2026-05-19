# from django.urls import path
# from .import views

# urlpatterns=[
#     path('list/', views.courseList),
#     path('add/', views.addCourse),
#     path('update/<id>/', views.updateCourse),
#     path('delete/<id>/', views.deleteCourse),
# ]

from rest_framework.routers import DefaultRouter
from .views import CourseView

router = DefaultRouter()
router.register(r'api/course', CourseView, basename='course')
urlpatterns = router.urls