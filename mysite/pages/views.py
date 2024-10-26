from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import Payment
from rest_framework import status
# Create your views here.   
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def terms_view(request):
    return render(request, 'terms.html')
def privacy_policy(request):
    return render(request, 'privacy.html')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_transaction(request):
    # Пример данных транзакции
    data = {
        'transaction_id': 'tx123',
        'status': 'created',
        'amount': request.data.get('amount'),
        'currency': request.data.get('currency')
    }
    return Response(data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_transaction_status(request, transaction_id):
    # Пример проверки статуса транзакции
    data = {
        'transaction_id': transaction_id,
        'status': 'completed'  # Здесь может быть логика для реального статуса
    }
    return Response(data)



@api_view(['POST'])
def initiate_payment(request):
    user_id = request.data.get('user_id')
    amount = request.data.get('amount')
    currency = request.data.get('currency', 'USD')  # По умолчанию USD
    
    # Создаем запись в базе данных для платежа
    payment = Payment.objects.create(
        user_id=user_id,
        transaction_id="some_unique_id",  # Тебе нужно сгенерировать или получить ID от платёжной системы
        amount=amount,
        currency=currency,
        status='initiated'
    )
    
    return Response({"status": "payment initiated", "transaction_id": payment.transaction_id})

@api_view(['POST'])
def verify_payment(request):
    # Логика проверки транзакции от платёжной системы
    payment_status = request.data.get('status')
    # Логика сохранения или проверки статуса в базе данных
    return Response({"status": "payment verified"})

@api_view(['GET'])
def payment_status(request, transaction_id):
    # Логика получения статуса платежа
    try:
        payment = Payment.objects.get(transaction_id=transaction_id)
        return JsonResponse({"status": payment.status})
    except Payment.DoesNotExist:
        return JsonResponse({"error": "Transaction not found"}, status=404)