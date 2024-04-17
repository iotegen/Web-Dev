from django.urls import path, re_path
from api.views import company_list,company_detail,vacancy_list,vacancy_detail,company_vacancies,top_ten_vacancies
from api.views import VacancyListCreateAPIView,VacancyRetrieveUpdateDestroyAPIView,CompanyListCreateAPIView,CompanyRetrieveUpdateDestroyAPIView,CompanyVacancyListAPIView,TopTenVacanciesAPIView

urlpatterns = [
    # path('companies/',company_list),
    # path('companies/<int:pk>/',company_detail),
    # path('vacancies/',vacancy_list),
    # path('vacancies/<int:pk>/',vacancy_detail),
    # path('companies/<int:id>/vacancies/', company_vacancies),
    # path('vacancies/top_ten/', top_ten_vacancies),



    path('vacancies/',VacancyListCreateAPIView.as_view()),
    path('vacancies/<int:pk>/',VacancyRetrieveUpdateDestroyAPIView.as_view()),
    path('companies/',CompanyListCreateAPIView.as_view()),
    path('companies/<int:pk>/',CompanyRetrieveUpdateDestroyAPIView.as_view()),
    path('companies/<int:id>/vacancies/', CompanyVacancyListAPIView.as_view()),
    path('vacancies/top_ten/', TopTenVacanciesAPIView.as_view()),

]