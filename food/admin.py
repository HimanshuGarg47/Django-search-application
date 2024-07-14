from django.contrib import admin
from .models import Restaurant, Dish

class DishInline(admin.TabularInline):
    model = Dish
    extra = 1

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    inlines = [DishInline]
    search_fields = ('name', 'location')

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')
    list_filter = ('restaurant',)
    search_fields = ('name', 'restaurant__name')

