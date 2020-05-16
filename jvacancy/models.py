from django.db import models

# Create your models here.

class Vacancy(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=64)
	specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
	company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
	skills = models.CharField(max_length=64)
	description = models.CharField(max_length=256)
	salary_min = models.IntegerField()
	salary_max = models.IntegerField()
	published_at = models.DateField()

class Company(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64)
	location = models.CharField(max_length=64)
	logo = models.CharField(max_length=64)
	description = models.CharField(max_length=256)
	employee_count = models.IntegerField()

class Specialty(models.Model):
	id = models.AutoField(primary_key=True)
	code = models.CharField(max_length=64)
	title = models.CharField(max_length=64)
	picture = models.CharField(max_length=128)