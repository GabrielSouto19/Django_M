from django.contrib import admin
from cars.models import Car,Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",) 
    search_fields = ("Não encontrado" ,)

class CarAdmin(admin.ModelAdmin):
    list_display = ("model","brand","factory_year","model_year","value") 
    search_fields = ("model","Brand" )



admin.site.register(Car,CarAdmin)

admin.site.register(Brand,BrandAdmin)
