from django import forms
from basic_app.models import Exam
from django.contrib.auth.models import User
from django.contrib import auth
class ExamForm(forms.ModelForm):

    class Meta():
        model=Exam
        fields=('name','branch','semester','sessional','year','file')




class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')
