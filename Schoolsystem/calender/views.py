from .models import Calendar
from django.shortcuts import render
from .forms import EventRegistrationForm

def register_event(request):
    if request.method=="POST":
        form=EventRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=EventRegistrationForm()
    return render(request,"register_event.html",{"form":form})
        
def event_list(request):
    events=Calendar.objects.all
    return render(request,"event_list.html",{"events":events})




# Create your views here.


# Create your views here.
