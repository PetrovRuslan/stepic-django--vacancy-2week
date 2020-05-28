from django import forms

class SignupForm(forms.Form):
	login = forms.EmailField()
	password = forms.CharField(label='Destination Address')
    
class LoginForm(forms.Form):
	login = forms.EmailField()
	password = forms.CharField(max_length=32)