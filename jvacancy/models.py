from django.db import models
from django.contrib.auth.models import User
from stepic_vacancy.settings import MEDIA_SPECIALITY_IMAGE_DIR, MEDIA_COMPANY_IMAGE_DIR

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
    location = models.CharField(max_length=64, null=True, blank=True)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR)
    description = models.CharField(max_length=256, null=True, blank=True)
    employee_count = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None,
        null=True, blank=True)


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR)


class Application(models.Model):
    written_username = models.CharField(max_length=64)
    written_phone = models.CharField(max_length=64)
    written_cover_letter = models.CharField(max_length=256)
    vacancy = models.ForeignKey('Vacancy', on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', blank=True, null=True)