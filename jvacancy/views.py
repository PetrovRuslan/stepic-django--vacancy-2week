from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views import View
from jvacancy.models import Vacancy, Company, Specialty, Application
from jvacancy.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from django.shortcuts import redirect

# Create your views here.

class MainView(View):
    def get(self, request, *args, **kwargs):
        specialty_dict = {}
        specialty_list = Specialty.objects.values_list('title', 'code', 'picture')
        for specialty in specialty_list:
            specialty_dict[specialty[0]] = {'quantity':len(Vacancy.objects.filter(specialty__title=specialty[0])), 'code': specialty[1], 'picture': specialty[2]}

        company_dict = {}
        company_list = Company.objects.values_list('name', 'logo', 'id')
        for company in company_list:
            company_dict[company[0]] = {'quantity': len(Vacancy.objects.filter(company__name=company[0])), 'logo': company[1], 'id': company[2]}

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
        vacancy_response_form = VacacyResponseForm()
        vacancy = Vacancy.objects.get(id=id)
        return render(
            request, 'jvacancy/vacancy.html', context={
                'vacancy_response_form': vacancy_response_form,
                'vacancy': vacancy,
            }
        )


class SendApplicationView(View):
    def post(self, request, vacancy_id, *args, **kwargs):
        vacancy_responce = VacacyResponseForm(request.POST)
        vacancy = Vacancy.objects.get(id=vacancy_id)
        logged_in_user = request.user
        if vacancy_responce.is_valid():
            data = vacancy_responce.cleaned_data
            if request.user.is_authenticated:
                application = Application.objects.create(written_username=data['written_username'], written_phone=data['written_phone'], written_cover_letter=data['written_cover_letter'], vacancy=vacancy, user=logged_in_user)
                return render(
                    request, 'jvacancy/sent.html'
                )
            else:
                application = Application.objects.create(written_username=data['written_username'], written_phone=data['written_phone'], written_cover_letter=data['written_cover_letter'], vacancy=vacancy)
                return render(
                    request, 'jvacancy/sent.html'
                )


class MyCompanyView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logged_in_user = request.user.get_username()
            user_company = Company.objects.filter(owner__username=logged_in_user)
            create_company_form = CreateCompanyForm(request.POST, request.FILES)
            # value_user_companies = len(user_companies)
            if len(user_company):
                return render(
                    request, 'jvacancy/company-edit.html', context={
                        'user_company': user_company,
                        'create_company_form': create_company_form,
                    }
                )
            else:
                return render(
                    request, 'jvacancy/company-create.html', context={
                        'create_company_form': create_company_form,
                    }
                )
        else:
            return redirect('/login')


class CreateCompanyView(View):
    def get(self, request, *args, **kwargs):
        edit_company_form = ""
        return render(
            request, 'jvacancy/company-edit.html', context={
            }
        )

class MyVacanciesView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'jvacancy/vacancies.html', context={
            }
        )


class MyVacancyView(View):
    def get(self, request, vacancy_id, *args, **kwargs):
        return render(
            request, 'jvacancy/vacancy.html', context={
                
            }
        )


class MyRegisterView(View):
    def get(self, request, *args, **kwargs):
        sign_up = SignupForm()
        return render(
            request, 'jvacancy/register.html', context={
                'sign_up': sign_up,
            }
        )


class MySignupView(View):
    def post(self, request, *args, **kwargs):
        sign_up = SignupForm(request.POST)
        if sign_up.is_valid():
            data = sign_up.cleaned_data
            User.objects.create_user(first_name=data['first_name'], last_name=data['last_name'], username=data['login'], password=data['password'])
            return redirect('/login')


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'jvacancy/login.html'

