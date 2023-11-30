# Generated by Django 4.2.6 on 2023-11-30 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('Собственный IT-продукт', 'Собственный IT-продукт'), ('Заказная разработка', 'Заказная разработка'), ('Другое', 'Другое'), ('Неопределенный', 'Неопределенный')], max_length=100, verbose_name='category_name')),
                ('style_name', models.CharField(default='', max_length=100, verbose_name='style_name')),
                ('description', models.TextField(default='', verbose_name='description')),
            ],
            options={
                'verbose_name': 'CompanyCategory',
                'verbose_name_plural': 'CompanyCategories',
            },
        ),
        migrations.CreateModel(
            name='CompanySubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(choices=[('Стартапы с IT решениями', 'Стартапы с IT решениями'), ('Сопровождение популярных массовых ИТ продуктов', 'Сопровождение популярных массовых ИТ продуктов'), ('Веб-студии', 'Веб-студии'), ('Большие ИТ - компании', 'Большие ИТ - компании'), ('B2G', 'B2G'), ('Разработка игр', 'Разработка игр'), ('Неопределенный', 'Неопределенный')], max_length=100, verbose_name='subcategory_name')),
                ('style_name', models.CharField(default='', max_length=100, verbose_name='style_name')),
                ('description', models.TextField(default='', verbose_name='description')),
                ('company_category_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='companies.companycategory')),
            ],
            options={
                'verbose_name': 'CompanySubcategory',
                'verbose_name_plural': 'CompanySubcategories',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('logotype', models.ImageField(upload_to='companies/logo/img', verbose_name='logotype')),
                ('short_description', models.TextField(verbose_name='short_description')),
                ('url', models.CharField(max_length=200, verbose_name='url')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='companies.companysubcategory')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'company')},
            },
        ),
    ]
