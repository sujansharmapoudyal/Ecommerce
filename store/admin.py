from django.contrib import admin
from .models import Category,Products,Customer,Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email']

class AdminOrder(admin.ModelAdmin):
    list_display = ['product','customer','quantity','price','status']

# Register your models here.

admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order,AdminOrder)

