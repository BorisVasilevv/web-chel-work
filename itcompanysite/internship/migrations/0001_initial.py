# Generated by Django 4.2.6 on 2024-09-07 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0003_rename_tag_name_tag_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(verbose_name='date_start')),
                ('date_end', models.DateField(verbose_name='date_end')),
                ('description', models.TextField(default='', verbose_name='description')),
                ('company_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='companies.company')),
            ],
        ),
    ]
