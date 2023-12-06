from django.db import models
from .namehelper import CompanyName
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class Category(models.Model):
    CATEGORY_NAME = (
        (CompanyName.CONST_SELF_PRODUCT, CompanyName.CONST_SELF_PRODUCT),
        (CompanyName.CONST_CUSTOM_DEV, CompanyName.CONST_CUSTOM_DEV),
        (CompanyName.CONST_OTHER, CompanyName.CONST_OTHER),
        (CompanyName.CONST_NONE_TYPE, CompanyName.CONST_NONE_TYPE)
    )

    category_name = models.CharField('category_name', max_length=100, choices=CATEGORY_NAME)
    color = models.CharField('color', max_length=25, default="gray")
    description = models.TextField('description', default="")

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        match self.category_name:
            case CompanyName.CONST_SELF_PRODUCT:
                self.style_name = 'self_product'
            case CompanyName.CONST_CUSTOM_DEV:
                self.style_name = 'custom_dev'
            case CompanyName.CONST_OTHER:
                self.style_name = 'other'
            case CompanyName.CONST_NONE_TYPE:
                self.style_name = 'none_type'
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'CompanyCategory'
        verbose_name_plural = 'CompanyCategories'


class Subcategory(models.Model):
    SUBCATEGORY_NAME = (

        (CompanyName.CONST_STARTUP, CompanyName.CONST_STARTUP),
        (CompanyName.CONST_PROJECT_SUPPORT, CompanyName.CONST_PROJECT_SUPPORT),

        (CompanyName.CONST_WEB_STUDIO, CompanyName.CONST_WEB_STUDIO),
        (CompanyName.CONST_IT_COMPANY, CompanyName.CONST_IT_COMPANY),
        (CompanyName.CONST_B2G, CompanyName.CONST_B2G),

        (CompanyName.CONST_GAME_DEV, CompanyName.CONST_GAME_DEV),
        (CompanyName.CONST_NONE_TYPE, CompanyName.CONST_NONE_TYPE)
    )
    subcategory_name = models.CharField('subcategory_name', max_length=100, choices=SUBCATEGORY_NAME)
    color = models.CharField('color', max_length=25, default="gray")
    description = models.TextField('description', default="")
    company_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING,  default='')

    def __str__(self):
        return self.subcategory_name

    def save(self, *args, **kwargs):
        match self.subcategory_name:
            case CompanyName.CONST_SELF_PRODUCT:
                self.style_name = 'self_product'
            case CompanyName.CONST_STARTUP:
                self.style_name = 'startup'
            case CompanyName.CONST_PROJECT_SUPPORT:
                self.style_name = 'project_support'

            case CompanyName.CONST_CUSTOM_DEV:
                self.style_name = 'custom_dev'
            case CompanyName.CONST_WEB_STUDIO:
                self.style_name = 'web_studio'
            case CompanyName.CONST_IT_COMPANY:
                self.style_name = 'big_it_company'
            case CompanyName.CONST_B2G:
                self.style_name = 'b2g'

            case CompanyName.CONST_GAME_DEV:
                self.style_name = 'game_dev'
            case CompanyName.CONST_NONE_TYPE:
                self.style_name = 'none_type'
        super(Subcategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'CompanySubcategory'
        verbose_name_plural = 'CompanySubcategories'


class Company(models.Model):
    name = models.CharField('name', max_length=150)
    logotype = models.ImageField('logotype', upload_to='companies/logo/img')
    short_description = models.TextField('short_description')
    url = models.CharField('url', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class CompanyCategory(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default='')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'CompanyCategory'
        verbose_name_plural = 'CompanyCategories'
        unique_together = ('subcategory', 'company')


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'company')
