"""stepic_vacancy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jvacancy.views import MainView, VacanciesView, VacanciesCategoryView, CompanyView, VacancyView, SendApplicationView, MyCompanyView, MyVacanciesView, MyVacancyView, MyRegisterView, MySignupView, MyLoginView, CreateCompanyView, Application
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('vacancies', VacanciesView.as_view()),
    path('vacancies/cat/<str:category>', VacanciesCategoryView.as_view()),
    path('company/<int:company>', CompanyView.as_view()),
    path('vacancies/<int:id>', VacancyView.as_view()),
    path('vacancies/<int:vacancy_id>/send', SendApplicationView.as_view()),
    path('mycompany', MyCompanyView.as_view(), name='my_company'),
    path('mycompany/vacancies', MyVacanciesView.as_view()),
    path('mycompany/vacancies/<int:vacancy_id>', MyVacancyView.as_view()),
    path('create_company', CreateCompanyView.as_view(), name='create_company'),
    path('register', MyRegisterView.as_view()),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', MySignupView.as_view()),
    path('login', MyLoginView.as_view(), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
