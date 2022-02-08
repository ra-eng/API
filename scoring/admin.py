from django.contrib import admin
from scoring.models import Employee
# Register your models here.
class Employees(admin.ModelAdmin):
    list_display= ("id","includeAt", "employeedId", "employerId" )
    list_display_links= ("includeAt", "employeedId", "employerId")
    search_fields= ("employeedId",)
    list_per_page=50

admin.site.register(Employee,Employees )
