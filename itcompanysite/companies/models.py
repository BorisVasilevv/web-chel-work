from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField('name', max_length=150)
    logotype = models.ImageField('logotype', upload_to='logo/img')
    short_description = models.TextField('short_description')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

