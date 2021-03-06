from .models import Trainer
from trainer.models import Trainer
from django import forms
from django.shortcuts import render
from .forms import TrainerRegistrationForm

def register_trainer(request):
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=TrainerRegistrationForm()
    return render(request,"register_trainer.html",{"form":form})
def trainer_list(request):
    trainers=Trainer.objects.all
    return render(request,"trainer_list.html",{"trainers":trainers})

