from django.db import models
from django.db import models

from django.contrib.auth import get_user_model

from companies.models import Company


# Create your models here.
class Intership(models.Model):

    date_start = models.DateField('date_start')
    date_end = models.DateField('date_end')
    description = models.TextField('description', default="")
    company_id = models.ForeignKey(Company, on_delete=models.DO_NOTHING,  default='')


def __str__(self):
    return self.subcategory_name

    class Meta:
        verbose_name = 'Intership'
        verbose_name_plural = 'Interships'