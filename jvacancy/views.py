from django.shortcuts import render
from django.http import Http404
from django.views import View
from jvacancy.models import Vacancy, Company, Specialty


# Create your views here.

class MainView(View):
    def get(self, request, *args, **kwargs):
        specialty_dict = {}
        company_dict = {}

        specialty_code_list = list(Specialty.objects.values_list('code', 'title'))

        for code in specialty_code_list:
            specialty_dict[code[0]] = {'quantity': len(Vacancy.objects.filter(specialty__code=code[0])),
                                       'title': code[1], 'code': code[0]}

        company_list = Company.objects.values_list('name', 'id')

        for company_name in company_list:
            company_dict[company_name[0]] = {'id': company_name[1], 'logo': "https://place-hold.it/100x60",
                                             'vacancy_quantity': len(
                                                 Vacancy.objects.filter(company__name=company_name[0]))}

        return render(
            request, 'jvacancy/index.html', context={
                'company_dict': company_dict,
                'specialty_dict': specialty_dict,
            }
        )


class VacanciesView(View):
    def get(self, request, *args, **kwargs):
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
        title_category = Specialty.objects.get(code=category)
        vacancies_category = Vacancy.objects.filter(specialty__code=category)
        number_of_vacancies_category = len(vacancies_category)
        return render(
            request, 'jvacancy/category.html', context={
                'vacancies_category': vacancies_category,
                'number_of_vacancies_category': number_of_vacancies_category,
                'title_category': title_category,
            }
        )


class CompanyView(View):
    def get(self, request, company, *args, **kwargs):
        company_profile = Company.objects.get(id=company)
        vacancies_company = Vacancy.objects.filter(company__name=company_profile.name)
        number_of_vacancies_company = len(vacancies_company)
        return render(
            request, 'jvacancy/company.html', context={
                'company_profile': company_profile,
                'vacancies_company': vacancies_company,
                'number_of_vacancies_company': number_of_vacancies_company,
            }
        )


class VacancyView(View):
    def get(self, request, id, *args, **kwargs):
        vacancy = Vacancy.objects.get(id=id)
        return render(
            request, 'jvacancy/vacancy.html', context={
                'vacancy': vacancy,
            }
        )
