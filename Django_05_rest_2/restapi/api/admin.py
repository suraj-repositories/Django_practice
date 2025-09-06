from django.contrib import admin

from .models import Company, Employee

# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'active', 'location', 'added_date')
    search_fields = ('name', 'location')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')
    search_fields = ('name', 'email')
    list_filter = ('company',)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
