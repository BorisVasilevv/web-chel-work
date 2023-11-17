from django.contrib import admin
from .models import Company, CompanyType
# Register your models here.


class MyAdminModel(admin.ModelAdmin):
    exclude = ('style_name',)


admin.site.register(Company)
admin.site.register(CompanyType, MyAdminModel)
