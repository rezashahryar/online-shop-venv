from django.contrib import admin
from .models import Coupon
# Register your models here.

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'active', 'valid_from', 'valid_to', 'discount']
    list_filter = ['active', 'valid_to', 'valid_from']
    search_fields = ['code']