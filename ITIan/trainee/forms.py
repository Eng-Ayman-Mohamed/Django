from django import forms 
from .models import trainee
from course.models import course

class TraineeForm(forms.Form):
    firstName=forms.CharField( max_length=20, required=False)
    lastName= forms.CharField( max_length=20, required=False)
    numOfMonths=forms.IntegerField()
    track=forms.TextInput() 
    image =forms.ImageField()
    course=forms.ChoiceField( choices=[(c.id, c.name) for c in course.objects.all()], required=False)

class TraineeFormModel(forms.ModelForm):
    class Meta:
        model = trainee
        fields = '__all__'
        exclude = ('id','createdAt')