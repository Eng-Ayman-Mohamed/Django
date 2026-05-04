from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def traineeList (request):
    return render(request, 'trainee/list.html')

def addTrainee(request):
    return HttpResponse('add trainee')

def updateTrainee(request):
    return HttpResponse('update trainee')

def deleteTrainee(request):
    return HttpResponse('delete trainee')