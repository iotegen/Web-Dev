"""
URL configuration for hhback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from api.views import (
    CompanyListCreateAPIView,
    CompanyRetrieveUpdateDestroyAPIView,
    CompanyVacancyListAPIView,
    VacancyListCreateAPIView,
    VacancyRetrieveUpdateDestroyAPIView,
    TopTenVacanciesAPIView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/companies/', CompanyListCreateAPIView.as_view(), name='company-list-create'),
    path('api/companies/<int:id>/', CompanyRetrieveUpdateDestroyAPIView.as_view(), name='company-detail'),
    path('api/companies/<int:id>/vacancies/', CompanyVacancyListAPIView.as_view(), name='company-vacancy-list'),
    path('api/vacancies/', VacancyListCreateAPIView.as_view(), name='vacancy-list-create'),
    path('api/vacancies/<int:id>/', VacancyRetrieveUpdateDestroyAPIView.as_view(), name='vacancy-detail'),
    path('api/vacancies/top_ten/', TopTenVacanciesAPIView.as_view(), name='top-ten-vacancies'),
]
