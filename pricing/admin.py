from django.contrib import admin
from .models import Pricing
# Register your models here.


@admin.register(Pricing)
class AdminPricing(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'discount_price',
                    'membership_time', 'added_at', 'details']
    list_display_links = ['id', 'name', 'price', 'discount_price',
                          'membership_time', 'added_at', 'details']
