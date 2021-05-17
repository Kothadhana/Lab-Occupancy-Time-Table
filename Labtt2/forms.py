from django import forms
from django.forms import ModelForm
from Labtt2.models import Listing

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class LabForm(ModelForm):
    class Meta:
        model=Listing
        fields='__all__'
class UsRgt(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ['username']
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Your Username",
			"required":True
			})
		}

'''class LabForm(forms.Form):
    lab_name=forms.CharField(label='lab_name', max_length=100)
    systems=forms.IntegerField(label="systems")
    monm=forms.CharField(label='monm', max_length=100)
    mone=forms.CharField(label='mone', max_length=100)
    tuem=forms.CharField(label='tuem', max_length=100)
    tuee=forms.CharField(label='tuee', max_length=100)
    wedm=forms.CharField(label='wedm', max_length=100)
    wede=forms.CharField(label='wede', max_length=100)
    thum=forms.CharField(label='thum', max_length=100)
    thue=forms.CharField(label='thue', max_length=100)
    frim=forms.CharField(label='frim', max_length=100)
    frie=forms.CharField(label='frie', max_length=100)
    satm=forms.CharField(label='satm', max_length=100)
    sate=forms.CharField(label='sate', max_length=100)'''
