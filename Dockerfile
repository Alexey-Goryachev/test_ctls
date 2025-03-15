# Используем Python-образ
FROM python:3.11-slim

# Устанавливаем зависимости для сборки (если нужно)
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install poetry

# Задаем рабочую директорию
WORKDIR /app

# Копируем файлы с зависимостями
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false && poetry install --only main --no-interaction --no-ansi

# Копируем исходный код проекта
COPY . .

# Указываем PYTHONPATH
ENV PYTHONPATH="/app/blockchain_test"

# Собираем статические файлы
RUN python /app/blockchain_test/manage.py collectstatic --noinput

# Проводим миграции
RUN python /app/blockchain_test/manage.py migrate --noinput


# Открываем порт для Gunicorn
EXPOSE 8000
