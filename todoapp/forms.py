from . models import Todo
from django import forms

class TodoForm(forms.ModelForm):
    class  Meta:
        model=Todo
        fields=['name','proirety','date']