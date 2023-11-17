from django.db import models
from .namehelper import CompanyName


# Create your models here.


class CompanyType(models.Model):
    TYPE_NAME = (
        (CompanyName.CONST_SELF_PRODUCT, CompanyName.CONST_SELF_PRODUCT),
        (CompanyName.CONST_STARTUP, CompanyName.CONST_STARTUP),
        (CompanyName.CONST_PROJECT_SUPPORT, CompanyName.CONST_PROJECT_SUPPORT),

        (CompanyName.CONST_CUSTOM_DEV, CompanyName.CONST_CUSTOM_DEV),
        (CompanyName.CONST_WEB_STUDIO, CompanyName.CONST_WEB_STUDIO),
        (CompanyName.CONST_IT_COMPANY, CompanyName.CONST_IT_COMPANY),
        (CompanyName.CONST_B2G, CompanyName.CONST_B2G),

        (CompanyName.CONST_GAME_DEV, CompanyName.CONST_GAME_DEV),

        (CompanyName.CONST_STATE_STRUCTURE, CompanyName.CONST_STATE_STRUCTURE),

        (CompanyName.CONST_NONE_TYPE, CompanyName.CONST_NONE_TYPE)

    )
    type_name = models.CharField('type_name', max_length=100, choices=TYPE_NAME)
    style_name = models.CharField('style_name', max_length=100, default="")
    description = models.TextField('description', max_length=350, default="")

    def __str__(self):
        return self.type_name

    def save(self, *args, **kwargs):
        match self.type_name:
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
            case CompanyName.CONST_STATE_STRUCTURE:
                self.style_name = 'state_structure'
            case CompanyName.CONST_NONE_TYPE:
                self.style_name = 'none_type'
        super(CompanyType, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'CompanyType'
        verbose_name_plural = 'CompanyTypes'


class Company(models.Model):
    name = models.CharField('name', max_length=150)
    logotype = models.ImageField('logotype', upload_to='companies/logo/img')
    short_description = models.TextField('short_description')
    url = models.CharField('url', max_length=200)
    type = models.ForeignKey(CompanyType, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
