from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views import View

# Create your views here.

class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'jvacancy/index.html', context={
                # 'title': title,
                # 'subtitle': subtitle,
                # 'description': description,
                # 'departures': departures,
                # 'index_tours': index_tours,
            }
        )

class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'jvacancy/vacancies.html', context={
            }
        )

class VacanciesCategoryView(View):
    def get(self, request, category, *args, **kwargs):
        return render(
            request, 'jvacancy/vacancies.html', context={
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

