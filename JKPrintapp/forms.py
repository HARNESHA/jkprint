from dataclasses import fields
from pyexpat import model
from django import forms
from .models import newuser

class newuserForm(forms.ModelForm):
    class Meta:
        model=newuser
        fields='__all__'