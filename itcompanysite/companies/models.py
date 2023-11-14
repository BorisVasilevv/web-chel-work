from django.db import models

# Create your models here.

class CompanyType(models.Model):

    TYPE_NAME = (
        ('заказная разработка', 'Заказная разработка'),
        ('собственный IT-продукт', 'Собственный IT-продукт'),
        ('госструктуры', 'Госструктуры'),
        ('неопределенный', 'Неопределенный')
    )
    type_name = models.CharField('type_name', max_length=100, choices=TYPE_NAME)
    description = models.CharField('description', max_length=350, default="")

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = 'CompanyType'
        verbose_name_plural = 'CompanyTypes'

class Company(models.Model):
    name = models.CharField('name', max_length=150)
    logotype = models.ImageField('logotype', upload_to='companies/logo/img')
    short_description = models.TextField('short_description')
    url = models.CharField('url', max_length=200)
    type = models.ForeignKey(CompanyType, on_delete=models.DO_NOTHING, default=4)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'