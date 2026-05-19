from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import trainee
from course.models import course
from .forms import *
# Create your views here.

#generic view
class traineeList(ListView):    
    model=trainee
    template_name = "trainee/list.html"
    success_url = reverse_lazy('trainees')
    context_object_name = 'trainees'

def viewTrainee (request, id):
    traineeData = trainee.objects.get(id=id)
    return render(request, 'trainee/traineePage.html', {'trainee':traineeData})

#generic create view

class addNewTrainee(CreateView):
    model= trainee
    fields = ['firstName', 'lastName', 'numOfMonths','track', 'course' ]
    template_name = "trainee/newTrainee.html"
    success_url = reverse_lazy('trainees')


class UpdateTraineeView(UpdateView):
    model = trainee
    fields = ['firstName', 'lastName', 'numOfMonths', 'track', 'course', 'image'] # Added image since your model has it
    template_name = "trainee/update.html"
    success_url = reverse_lazy('trainees')
    
    pk_url_kwarg = 'id'

def deleteTrainee(request,id):
    if (trainee.objects.filter(id=id) ):
        trainee.objects.filter(id=id).delete()
        return redirect('trainees')
    else:
        return render(request,'trainee/list.html',context={'error':'book not found'})


#class based view
class addTrainee(View):
    def get(self, request):
        courses = course.objects.all()
        return render (request,'trainee/new.html', {'courses':courses})
    def post(self, request):
        trainee.objects.create(
            firstName=request.POST['firstName'],
            lastName=request.POST['lastName'],
            numOfMonths=request.POST['numOfMonths'],
            track=request.POST['track'],
            course=course.objects.get(id=request.POST['course'])
        )
        return redirect ('trainees')
