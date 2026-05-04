from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def traineeList (request):
    return render(request, 'trainee/list.html')

def addTrainee(request):
    return HttpResponse('add trainee')

def updateTrainee(request,id):
    return HttpResponse(f'update trainee with id: {id}')

def deleteTrainee(request,id):
    return HttpResponse('delete trainee with id: {id}')