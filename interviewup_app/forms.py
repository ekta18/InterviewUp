from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms

class createUserForm(UserCreationForm):
	username = forms.EmailField(max_length=254, required=True)
	# email = forms.CharField(widget=forms.TextInput(),max_length=254, required=True)
	password1 = forms.CharField(widget=forms.PasswordInput(),required=True)
	password2 = forms.CharField(widget=forms.PasswordInput(),required=True)

	class Meta:
		model=User
		fields=['username','password1','password2']


class LoginForm(forms.ModelForm):
	email = forms.EmailField(max_length = 254, required = True)
	password = forms.CharField(widget = forms.PasswordInput(), required = True)
	class Meta:
		model = User
		fields = ('email','password')

class FileForm(forms.ModelForm):
    class Meta:
        model= File
        fields= ["filepath"]

# class ResumeForm(forms.Form):
#     # name = forms.CharField()
#     file_field = forms.FilePathField(path = "media/files/")
#     class Meta:
#         model= File
#         fields= ["file_field"]

# class ResumeForm(forms.ModelForm):  
#     class Meta:  
#         model = ResumeFiles  
#         fields = "__all__"
