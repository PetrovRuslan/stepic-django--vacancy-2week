from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views import View
from jvacancy.models import *

# Create your views here.

class MainView(View):
	def get(self, request, *args, **kwargs):
		specialty_dict = {}
		company_dict = {}

		specialty_code_list = list(Specialty.objects.values_list('code', 'title'))

		for code in specialty_code_list:
			specialty_dict[code[0]] = {'quantity': len(Vacancy.objects.filter(specialty__code=code[0])), 'title': code[1]}

		company_list = (Company.objects.values_list('name'))

		for company_name in company_list:
			company_dict[company_name[0]] = {'logo':"https://place-hold.it/100x60", 'vacancy_quantity': len(Vacancy.objects.filter(company__name=company_name[0]))}
		
		return render(
			request, 'jvacancy/index.html', context={
				'company_dict': company_dict,
				'specialty_dict': specialty_dict,
			}
		)

class VacanciesView(View):
	def get(self, request, *args, **kwargs):
		# test = Specialty.objects.values_list('code', 'title')
		vacancies = Vacancy.objects.all()
		number_of_vacancies = len(vacancies)
		return render(
			request, 'jvacancy/vacancies.html', context={
				'vacancies': vacancies,
				'number_of_vacancies': number_of_vacancies,
			}
		)

class VacanciesCategoryView(View):
	def get(self, request, category, *args, **kwargs):
		test_dict = []
		vacancy_category = Vacancy.objects.filter(specialty__code=category)
		cat_code_list = Specialty.objects.values_list('code')
		cat_title_list = Specialty.objects.values_list('title')
		for vacancy in vacancy_category:
			test_dict.append(j.company.name)
		return render(
			request, 'jvacancy/category.html', context={
				'vacancy_category': vacancy_category,
				'test_dict': test_dict,
			}
		)

class CompanyView(View):
    def get(self, request, company, *args, **kwargs):
        return render(
            request, 'jvacancy/company.html', context={
            }
        )

class VacancyView(View):
    def get(self, request, id, *args, **kwargs):
        return render(
            request, 'jvacancy/vacancy.html', context={
            }
        )

