# Generated by Django 4.2.6 on 2024-02-11 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=150, verbose_name='street')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='CompanyTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='companies.company')),
                ('tag', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='companies.tag')),
            ],
            options={
                'verbose_name': 'CompanyTag',
                'verbose_name_plural': 'CompanyTags',
            },
        ),
    ]
