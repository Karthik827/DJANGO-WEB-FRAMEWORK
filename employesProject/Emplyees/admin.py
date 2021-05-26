from django.contrib import admin
from.models import Employee

class EmplyeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esalary','eaddress']

# Register your models here.
admin.site.register(Employee,EmplyeeAdmin)