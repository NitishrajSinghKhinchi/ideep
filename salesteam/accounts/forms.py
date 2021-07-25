from typing import Pattern
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import fields
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,UsernameField,AuthenticationForm
from django import forms
import re
from .models import CustomUser,Working,Client
from django.utils.translation import gettext,gettext_lazy as _

"""Various type of validators are created and I have created  basic validators for validated number"""
def mobile_check(value):
    print(value)
    if CustomUser.objects.filter(mobile_no=value).exists():
        raise forms.ValidationError("Phone number already registred")

def isValid(value):
    print(value)
    if not value.isnumeric():
        raise ValidationError("Mobile num not correct")
    patterns = re.compile("[7-9][0-9]{9}") 
    if not patterns.match(value):
        raise ValidationError("Mobile number should be 8225088069")

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    mobile_no = forms.CharField(validators=[mobile_check,isValid],label='Mobile No.',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'format:-8225088069'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = CustomUser
        fields=['mobile_no','email','password1','password2']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"),widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class Workingform(forms.ModelForm):
    class Meta:
        model = Working
        fields = ['area_visited', 'total_person', 'number_of_leads']
        labels = {'area_visited':'Area visited','total_person':'Total person visited','number_of_leads':'Number of clients'}

class Clientform(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name','dob','age','gender','family_member']
        labels = {'name':'Name','age':'Age','gender':'Gender','family_member':'Famiy Member'}
        widgets={'dob':forms.TextInput(attrs={'placeholder':'format:-2000-14-09'})}