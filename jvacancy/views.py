from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views import View

# Create your views here.

class MainView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Это главная страница")

class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Это список вакансий")

class VacanciesCategoryView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Это вакансии по категориям")

class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Это страница вакансии")

