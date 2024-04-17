from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

# Company CRUD function-based views
@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def company_detail(request, id):
    company = get_object_or_404(Company, pk=id)
    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = CompanySerializer(company, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({}, status=204)

def company_vacancies(request, id):
    company = get_object_or_404(Company, pk=id)

    if request.method == 'GET':
        vacancies = Vacancy.objects.filter(company=company)
        
        serializer = VacancySerializer(vacancies, many=True)

        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

# Vacancy CRUD function-based views

def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = VacancySerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def vacancy_detail(request, id):
    vacancy = get_object_or_404(Vacancy, pk=id)
    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = VacancySerializer(vacancy, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({}, status=204)

def top_ten_vacancies(request):
    if request.method == 'GET':
        top_vacancies = Vacancy.objects.order_by('-salary')[:10]

        serializer = VacancySerializer(top_vacancies, many=True)

        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)