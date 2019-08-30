from django import forms
from .models import Dishes
class Registration(forms.Form):
    name=forms.CharField()
    area=forms.CharField()
    city=forms.CharField()
    email=forms.EmailField()
    mobile=forms.CharField()

class login(forms.Form):
    name=forms.CharField()
    mobile=forms.CharField()

class ChannelForm(forms.ModelForm):
    class Meta:
        model=Dishes
        fields='__all__'
   