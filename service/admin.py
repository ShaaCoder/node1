from django.contrib import admin

# Register your models here.
from service.models import Employee

class EmployeeDetail(admin.ModelAdmin):
    list_display=("full_name","email_id","mob_num","password")


admin.site.register(Employee,EmployeeDetail)  