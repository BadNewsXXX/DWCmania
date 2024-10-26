from django.db import models
from django.utils import timezone

class Payment(models.Model):
    STATUS_CHOICES = (
        ('initiated', 'Initiated'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    
    user_id = models.IntegerField()  # Если используешь собственные ID пользователей
    transaction_id = models.CharField(max_length=255, unique=True)  # Уникальный идентификатор транзакции
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма платежа
    currency = models.CharField(max_length=10, default="USD")  # Валюта платежа, например, USD, BTC
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='initiated')  # Статус платежа
    created_at = models.DateTimeField(default=timezone.now)  # Время создания платежа
    updated_at = models.DateTimeField(auto_now=True)  # Время обновления статуса

    def __str__(self):
        return f"Payment {self.transaction_id} - {self.status}"

