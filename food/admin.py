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
    autocomplete_fields = ('restaurant',)


# from import_export import resources, fields
# from import_export.widgets import ForeignKeyWidget
# from .models import Restaurant, Dish, Location

# class RestaurantResource(resources.ModelResource):
#     class Meta:
#         model = Restaurant
#         fields = ('name', 'location')

# class DishResource(resources.ModelResource):
#     # name = fields.Field(column_name='name', attribute='name', widget=ForeignKeyWidget(Restaurant, field='name'))
#     restaurant = fields.Field(column_name='name', attribute='restaurant', widget=ForeignKeyWidget(Restaurant, field='name'))

#     class Meta:
#         model = Dish
#         fields = ('items', 'restaurant', 'location', 'price')

#     def before_import_row(self, row, **kwargs):
#         restaurant_name = row['name']
#         location = row['location']
#         restaurant = Restaurant.objects.get_or_create(name=restaurant_name, location=location)
#         json_dish = row['items']

