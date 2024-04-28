from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView
# Create your views here.

from .models import *

class HomePageView(ListView):
    model = Vacancy
    template_name = "index.html"
    context_object_name = "vacancy_list"
    
class CompanyDetailVIew(TemplateView):
    template_name = "educenter.html"

class VacancyDetailView(TemplateView):
    template_name = "vacancy-detail.html"