# Generated by Django 4.2.6 on 2023-11-07 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_company_logotype'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Company',
        ),
    ]