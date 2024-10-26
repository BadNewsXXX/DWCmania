from django.urls import path
from django.http import JsonResponse
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


def api_overview(request):
    return JsonResponse({"message": "Welcome to the API Overview"})

urlpatterns = [
    path('', api_overview, name='api_overview'),  # Добавляем этот путь для базового маршрута
    path('transaction/', views.create_transaction, name='create_transaction'),
    path('transaction/<str:transaction_id>/', views.get_transaction_status, name='get_transaction_status'),

    # Маршруты для получения токенов
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]