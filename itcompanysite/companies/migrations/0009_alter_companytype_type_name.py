# Generated by Django 4.2.6 on 2023-11-27 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0008_companytype_style_name_alter_company_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companytype',
            name='type_name',
            field=models.CharField(choices=[('Собственный IT-продукт', 'Собственный IT-продукт'), ('Стартапы с IT решениями', 'Стартапы с IT решениями'), ('Сопровождение популярных массовых ИТ продуктов', 'Сопровождение популярных массовых ИТ продуктов'), ('Заказная разработка', 'Заказная разработка'), ('Веб-студии', 'Веб-студии'), ('Большие ИТ - компании', 'Большие ИТ - компании'), ('B2G', 'B2G'), ('Разработка игр', 'Разработка игр'), ('Госструктуры', 'Госструктуры'), ('Неопределенный', 'Неопределенный')], max_length=100, verbose_name='type_name'),
        ),
    ]
