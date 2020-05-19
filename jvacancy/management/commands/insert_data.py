from django.core.management.base import BaseCommand
from jvacancy.models import Company, Vacancy, Specialty
from data import jobs, companies, specialties
from random import randint


class Command(BaseCommand):
    print('start insert data in DB')
    print('----------------------')

    def handle(self, *args, **kwargs):
        for company in companies:
            company = Company.objects.create(name=company['title'], employee_count=randint(10, 200),
                                             logo="https://place-hold.it/100x60")

        for specialty in specialties:
            specialty = Specialty.objects.create(code=specialty['code'], title=specialty['title'],
                                                 picture="https://place-hold.it/100x60")

        for company1 in companies:
            for job in jobs:
                if company1['title'] == job['company']:
                    company = Company.objects.get(name=company1['title'])
                    job = Vacancy.objects.create(title=job['title'], specialty=specialty, company=company,
                                                 salary_min=job['salary_from'], salary_max=job['salary_to'],
                                                 published_at=job['posted'], description=job['desc'])

        for specialty1 in specialties:
            for job in jobs:
                if specialty1['code'] == job['cat']:
                    specialty = Specialty.objects.get(code=specialty1['code'])
                    job = Vacancy.objects.update(specialty=specialty)
