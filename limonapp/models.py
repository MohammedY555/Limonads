from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.category


class Subcategory(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subcategory


class Condition(models.Model):
    condition = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.condition


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE, null=True)
    images = models.JSONField(default=dict)
    attributes = models.JSONField(default=dict)
    payment_status = models.ForeignKey('PaymentStatus', on_delete=models.CASCADE, default=6)
    advertise_status = models.ForeignKey('AdvertiseStatus', on_delete=models.CASCADE, default=7)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class AdvertiseStatus(models.Model):
    adv_status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adv_status


class PaymentStatus(models.Model):
    pay_status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pay_status


class Payment(models.Model):
    advertisement = models.ForeignKey('Advertisement', on_delete=models.CASCADE)
    payment_status = models.ForeignKey('PaymentStatus', on_delete=models.CASCADE)
    pay_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    pay_method = models.ForeignKey('PayMethod', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)


class PayMethod(models.Model):
    payment_method = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.payment_method
