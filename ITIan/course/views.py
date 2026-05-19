from django.shortcuts import render
from .models import course
from rest_framework.viewsets import ModelViewSet
from .serializer import CourseSerializer

from rest_framework.permissions import IsAuthenticated


class CourseView( ModelViewSet):
    queryset = course.objects.all()
    serializer_class = CourseSerializer

    permission_classes = [IsAuthenticated]


# Create your views here.
# @login_required
# def courseList(request):
#     courses = course.objects.all()
#     return render(request, 'course/list.html',{'courses':courses})
# @login_required
# def addCourse(request):
#     return HttpResponse('add Course')
# @login_required
# def updateCourse(request,id):
#     return HttpResponse(f'update Course with id: {id}')
# @login_required
# def deleteCourse(request,id):
#     return HttpResponse(f'delete Course with id: ${id}')