from django.shortcuts import render
from django.http import HttpResponse
from .models import trainee
# Create your views here.

def traineeList (request):
    trainees = trainee.objects.all()
    return render(request, 'trainee/list.html', {'trainees':trainees})

def viewTrainee (request, id):
    traineeData = trainee.objects.get(id=id)
    return render(request, 'trainee/traineePage.html', {'trainee':traineeData})

def addTrainee(request):
    return HttpResponse('add trainee')

def updateTrainee(request,id):
    return HttpResponse(f'update trainee with id: {id}')

def deleteTrainee(request,id):
    return HttpResponse('delete trainee with id: {id}')

#view by id , add, delete