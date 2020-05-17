from django.core.management.base import BaseCommand
from django.utils import timezone
from jvacancy.models import Company, Vacancy, Specialty
from data import *
from random import randint


class Command(BaseCommand):
	print('start insert data in DB')
	print('----------------------')
	def handle(self, *args, **kwargs):
		for company in companies:
			company = Company.objects.create(name=company['title'], employee_count=randint(10, 200))
		for specialty in specialties:
			specialty = Specialty.objects.create(code=specialty['code'], title=specialty['title'])
		for job in jobs:
			print(job)
			job = Vacancy.objects.create(title=job['title'], salary_min=job['salary_from'], salary_max=job['salary_to'], published_at=job['posted'], description=job['desc'])
			# job.save()
		print('----------------------')
		print('end insert data in DB')