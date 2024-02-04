# Используйте официальный образ Python
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /web-chel-work

# Копируем зависимости проекта
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем текущий каталог в контейнер
COPY . .

# Определяем порт, который будет слушать контейнер
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "./itcompanysite/manage.py", "runserver", "0.0.0.0:8000"]
