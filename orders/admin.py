from django.contrib import admin

# Register your models here.
from .models import Product, Order, RefundRequest

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "in_stock")
    search_fields = ("name", "category")
    list_filter = ("category", "in_stock")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product_name", "amount", "status", "created_at")
    search_fields = ("user__username", "product_name", "status")
    list_filter = ("status", "created_at")

class RefundRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "user", "reason", "status", "created_at")
    search_fields = ("order__id", "user__username", "status")
    list_filter = ("status", "created_at")

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(RefundRequest, RefundRequestAdmin)