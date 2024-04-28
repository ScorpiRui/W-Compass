from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, CompanyDetailVIew, VacancyDetailView

app_name = "main"

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('company/', CompanyDetailVIew.as_view(), name='company'),
    path('vacancy/', VacancyDetailView.as_view(), name='vacancy'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)