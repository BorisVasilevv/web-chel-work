# Generated by Django 4.2.6 on 2023-11-11 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_alter_companytype_options_company_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companytype',
            name='description',
            field=models.CharField(default='', max_length=350, verbose_name='description'),
        ),
    ]