from django.contrib import admin
from .models import Category, Subcategory, Condition, Advertisement, AdvertiseStatus, \
 PaymentStatus, Payment, PayMethod

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Condition)
admin.site.register(Advertisement)
admin.site.register(AdvertiseStatus)
admin.site.register(PaymentStatus)
admin.site.register(Payment)
admin.site.register(PayMethod)
