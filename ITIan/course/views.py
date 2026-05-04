from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courseList(request):
    return render(request, 'course/list.html')

def addCourse(request):
    return HttpResponse('add Course')

def updateCourse(request,id):
    return HttpResponse(f'update Course with id: {id}')

def deleteCourse(request,id):
    return HttpResponse(f'delete Course with id: ${id}')