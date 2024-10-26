from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # Маршрут для главной страницы
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms_view, name='terms'),
    path('privacy/', views.privacy_policy, name='privacy'),
]
