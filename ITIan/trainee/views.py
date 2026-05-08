from django.shortcuts import render,redirect
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
    if request.method == 'POST':

        trainee.objects.create(
            firstName=request.POST['firstName'],
            lastName=request.POST['lastName'],
            numOfMonths=request.POST['numOfMonths'],
            track=request.POST['track'],

        )
        return redirect ('trainees')
    return render (request,'trainee/new.html')

def updateTrainee(request,id):
    return HttpResponse(f'update trainee with id: {id}')

def deleteTrainee(request,id):
    if (trainee.objects.filter(id=id) ):
        trainee.objects.filter(id=id).delete()
        return redirect('trainees')
    else:
        return render(request,'trainee/list.html',context={'error':'book not found'})

#view by id , add, delete