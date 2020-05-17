from django.core.management.base import BaseCommand
from jvacancy.models import *
from data import *


class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		# print(Vacancy.objects)
		# specialty_list = list(Specialty.objects.values_list('title'))
		# specialty_list = list(Specialty.objects.values_list('title'))
		# print(type(specialty_list))
		# print(specialty_list[0])
		# for vacancy in Vacancy.objects:
		# 	print(vacancy)
		# for item in specialty_list:
		# 	print(str(item))
		# 	print(type(str(item)))
		# company_list = list(Company.objects.values_list('name'))
		# print(company_list[0])
		# test = Vacancy.objects.filter(company__name__contains='workiro')
		# test = Vacancy.objects.filter(specialty__code='frontend')
		# test1 = Company.objects.filter(name='primalassault')
		# print(Company.objects.filter(name='workiro').first().vacancies.all())
		# print(test1)
		# print(test)
		# print(Specialty.objects.values_list('name'))
		# for vacancy in Vacancy.objects:
		# print(Company.objects.filter(name='workiro')
		test = Vacancy.objects.filter(specialty__code='backend')
		print(test)