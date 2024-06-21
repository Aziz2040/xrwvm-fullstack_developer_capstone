from django.contrib import admin
from .models import CarMake, CarModel


# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)

# Register your models here.

# CarModelInline class
class CarModelInline(admin.TabularInline):  # Or StackedInline for vertical editing
    model = CarModel
    extra = 1  # Optional: Pre-populate with one blank car model form
# CarModelAdmin class
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
# CarMakeAdmin class with CarModelInline

# Register models here
