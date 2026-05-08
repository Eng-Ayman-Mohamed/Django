from django.shortcuts import render
from django.http import HttpResponse
from .models import course
# Create your views here.

def courseList(request):
    courses = course.objects.all()
    return render(request, 'course/list.html',{'courses':courses})

def addCourse(request):
    return HttpResponse('add Course')

def updateCourse(request,id):
    return HttpResponse(f'update Course with id: {id}')

def deleteCourse(request,id):
    return HttpResponse(f'delete Course with id: ${id}')