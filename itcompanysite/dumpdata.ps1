..\venv\Scripts\Activate

python manage.py dumpdata companies.Address --indent 2 --output companies/fixtures/address_data.json --format=json
python -c "import json; data = json.load(open('companies/fixtures/address_data.json', encoding='cp1251')); json.dump(data, open('companies/fixtures/address_data_utf8.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)"
del companies/fixtures/address_data.json

python manage.py dumpdata companies.Category --indent 2 --output companies/fixtures/categories_data.json --format=json
python -c "import json; data = json.load(open('companies/fixtures/categories_data.json', encoding='cp1251')); json.dump(data, open('companies/fixtures/categories_data_utf8.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)"
del companies/fixtures/categories_data.json

python manage.py dumpdata companies.City --indent 2 --output companies/fixtures/cities_data.json --format=json
python -c "import json; data = json.load(open('companies/fixtures/cities_data.json', encoding='cp1251')); json.dump(data, open('companies/fixtures/cities_data_utf8.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)"
del companies/fixtures/cities_data.json

python manage.py dumpdata companies.Company --indent 2 --output companies/fixtures/companies_data.json --format=json
python -c "import json; data = json.load(open('companies/fixtures/companies_data.json', encoding='cp1251')); json.dump(data, open('companies/fixtures/companies_data_utf8.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)"
del companies/fixtures/companies_data.json

python manage.py dumpdata companies.CompanyAddress --indent 2 --output companies/fixtures/company_address_data.json --format=json
python -c "import json; data = json.load(open('companies/fixtures/company_address_data.json', encoding='cp1251')); json.dump(data, open('companies/fixtures/company_address_data_utf8.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)"
del companies/fixtures/company_address_data.json

python manage.py dumpdata companies.CompanyCategory --indent 2 --output companies/fixtures/company_categories_data.json --format=json
python -c "import json; data = json.load(open('companies/fixtures/company_categories_data.json', encoding='cp1251')); json.dump(data, open('companies/fixtures/company_categories_data_utf8.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)"
del companies/fixtures/company_categories_data.json

python manage.py dumpdata companies.Subcategory --indent 2 --output companies/fixtures/subcategories_data.json --format=json
python -c "import json; data = json.load(open('companies/fixtures/subcategories_data.json', encoding='cp1251')); json.dump(data, open('companies/fixtures/subcategories_data_utf8.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)"
del companies/fixtures/subcategories_data.json