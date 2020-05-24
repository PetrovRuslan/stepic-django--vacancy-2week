from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.ImageField(upload_to='MEDIA_COMPANY_IMAGE_DIR')
    description = models.CharField(max_length=256)
    employee_count = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None,
        null=True)


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.ImageField(upload_to='MEDIA_SPECIALITY_IMAGE_DIR')


class Application(models.Model):
    written_username = models.CharField(max_length=64)
    written_phone = models.CharField(max_length=64)
    written_cover_letter = models.CharField(max_length=256)
    vacancy = models.ForeignKey('Vacancy', on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')


class PostcardForm(forms.Form):
    address = forms.CharField(label='Destination Address')
    author = forms.CharField(min_length=3)
    compliment = forms.CharField(max_length=1024)
    date_of_delivery = forms.DateField(input_formats=['%Y/%m/%d'])
    email = forms.EmailField()