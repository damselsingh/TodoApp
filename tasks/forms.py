from .models import task
from django import forms
from django.forms import ModelForm

class TaskForm(forms.ModelForm):


    class Meta:
        model= task
        fields = '__all__'