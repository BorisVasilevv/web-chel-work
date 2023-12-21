from django.contrib import admin
from .models import Company, Category, Subcategory, CompanyCategory, Favorite, Address, City, CompanyAddress
# Register your models here.


class MyAdminModel(admin.ModelAdmin):
    exclude = ('style_name',)


admin.site.register(Company)
admin.site.register(Favorite)
admin.site.register(Category, MyAdminModel)
admin.site.register(Subcategory, MyAdminModel)
admin.site.register(CompanyCategory)
admin.site.register(Address)
admin.site.register(City)
admin.site.register(CompanyAddress)
