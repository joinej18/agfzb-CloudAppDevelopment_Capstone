from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    fields = ["name", "id", " car model"]


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ["type", "id", "name"]

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display= ['Car Make']
    inline=[CarModelInline]

# Register models here
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake)
