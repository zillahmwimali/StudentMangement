from django import forms
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from .models import Calendar

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model=Calendar
        fields="__all__"