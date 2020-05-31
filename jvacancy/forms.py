from django import forms

class SignupForm(forms.Form):
	login = forms.EmailField()
	password = forms.CharField(label='Destination Address')
    
class LoginForm(forms.Form):
	login = forms.EmailField()
	password = forms.CharField(max_length=32)

class VacacyResponseForm(forms.Form):
	written_username = forms.CharField(max_length=64)
	written_phone = forms.CharField(max_length=64)
	written_cover_letter = forms.CharField(max_length=256)