# Generated by Django 4.2.6 on 2023-12-05 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_alter_category_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(default='gray', max_length=25, verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='color',
            field=models.CharField(default='gray', max_length=25, verbose_name='color'),
        ),
    ]