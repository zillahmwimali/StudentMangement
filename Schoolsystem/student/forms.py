from django import forms
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"