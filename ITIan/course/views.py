from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courseList(request):
    return render(request, 'course/list.html')

def addCourse(request):
    return HttpResponse('add Course')

def updateCourse(request):
    return HttpResponse('update Course')

def deleteCourse(request):
    return HttpResponse('delete Course')