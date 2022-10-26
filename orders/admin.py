from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

class OderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'address', 'postcode', 'city', 'paid', 'created', 'updated']
    list_filter = ('paid', 'created', 'updated')
    inlines = [OderItemInline]