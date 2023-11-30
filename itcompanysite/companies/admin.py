from django.contrib import admin
from .models import Company, CompanyType, Favorite
# Register your models here.


class MyAdminModel(admin.ModelAdmin):
    exclude = ('style_name',)


admin.site.register(Company)
admin.site.register(Favorite)
admin.site.register(CompanyType, MyAdminModel)
