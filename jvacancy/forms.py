from django import forms

class SignupForm(forms.Form):
	first_name = forms.CharField(max_length=32)
	last_name = forms.CharField(max_length=32)
	login = forms.EmailField()
	password = forms.CharField(label='Destination Address')
    
class LoginForm(forms.Form):
	login = forms.EmailField()
	password = forms.CharField(max_length=32)

class VacacyResponseForm(forms.Form):
	written_username = forms.CharField(max_length=64)
	written_phone = forms.CharField(max_length=64)
	written_cover_letter = forms.CharField(max_length=256)

class CreateCompanyForm(forms.Form):
	company_name = forms.CharField(max_length=64)
	# company_logo = forms.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR)
	company_employes = forms.IntegerField()
	company_geo = forms.CharField(max_length=64)
	company_description = forms.CharField(max_length=512)
# class 