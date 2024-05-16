from django.contrib import admin
from fsd_app.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','email','mobile','address']
    list_filter=['address']

admin.site.register(Student,StudentAdmin)