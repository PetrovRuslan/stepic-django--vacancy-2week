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
		# test = Vacancy.objects.filter(specialty__code='backend')
		# specialty_code_list = list(Specialty.objects.values_list('code'))
		# print(specialty_code_list)
		# for item in specialty_code_list:
		# 	print(item[0])
		# # print(test)
		# specialty_dict = {}
		# specialty_title_list = list(Specialty.objects.values_list('title'))
		# specialty_code_list = list(Specialty.objects.values_list('code', 'title'))
		# for code in specialty_code_list:
		# 	specialty_dict[code[0]] = {'quantity': len(Vacancy.objects.filter(specialty__code=code[0])), 'title': code[1]}
		# 	# print(specialty_dict[code])
		# print(specialty_code_list)
		# print(specialty_dict)
		# company_list = (Company.objects.values_list('name'))
		# print(company_list)
		# company_dict = {}

		# for company_name in company_list:
		# 	company_dict[company_name[0]] = {'logo':"https://place-hold.it/100x60", 'vacancy_quantity': len(Vacancy.objects.filter(company__name=company_name[0]))}

		# # print(specialty_dict['title'])
		# print(company_dict)

		# test = Company.objects.all().values()
		# test2 = Specialty.objects.all().values()
		# dict_test = {}
		# for i in test:
		# 	dict_test
		# test = Specialty.objects.all()
		# dict_test = {}
		# print(Vacancy.objects.all())
		# category = "frontend"
		# vac = Vacancy.objects.filter(specialty__code="backend")
		# print(vac)
		# for j in vac:
		# 	print(j.company.name)
		# company_name_list = Specialty.objects.values_list('code', 'title')
		# print(company_name_list)
		# vacancies = Vacancy.objects.all().values()
		# print(vacancies)
		# for i in vacancies:
		# 	print(i['title'])
		# quantity_vacancies = len(vacancies)
		# print(quantity_vacancies)
		# category = "backend"
		# acancy_category = Vacancy.objects.filter(specialty__code=category)
		# print(acancy_category)
		# print(test)
		# for i in test:
		# 	print(i.code)
		# 	dict_test[i.code] = Vacancy.objects.filter(specialty__code=i.code)
		# print(dict_test)
		# for elem in dict_test:
		# 	print(dict_test[elem])
		# 	print('---')
		# vacancy_category = Vacancy.objects.all().values()
		# print(vacancy_category)
		# print(Vacancy.objects.all(specialty__code))
		# print(test)
		# list_test = []
		# for i in test:
		# 	# dict_test = Vacancy.objects.get() 
		# 	print(i['id'])
		# 	print('---')
		# 	list_test.append(Vacancy.objects.update(id=i['id'], specialty__title)) 
		# print(list_test)
		# for j in list_test:
		# 	print(j.specialty)
		# id_list = Vacancy.objects.format()
		# company = 3
		# company_profile = Company.objects.get(id=company)
		company_vacancy = Company.objects.filter(owner__username = 'test@test.test')
		print(company_vacancy)
		# number_of_vacancies_category = len(company_vacancy)
		# print(company_profile.name)
		# print(company_vacancy)
		# print(number_of_vacancies_category)
		# print('------------------')
		# for i in company_vacancy:
		# 	print(i.title)

