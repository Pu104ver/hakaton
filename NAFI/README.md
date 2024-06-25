

# NAFI Project

## Описание

Этот проект представляет собой платформу для управления курсами и встречами с использованием Django и PostgreSQL. Он включает в себя регистрацию пользователей, создание и управление встречами, уведомления и многое другое.

## Требования

- Python 3.12+
- PostgreSQL
- pip
- virtualenv

## Установка

### Шаг 1: Клонирование репозитория

```bash
git clone https://github.com/yourusername/nafi-project.git
cd nafi-project
```

### Шаг 2: Создание и активация виртуального окружения

```bash
python -m venv venv
source venv/bin/activate # Для Windows используйте `venv\Scripts\activate`
```

### Шаг 3: Установка зависимостей

```bash
pip install -r requirements.txt
```

### Шаг 4: Настройка базы данных

Убедитесь, что у вас установлен и запущен PostgreSQL. Создайте базу данных и пользователя с правами доступа.

```sql
CREATE DATABASE nafi;
CREATE USER admin WITH PASSWORD 'admin';
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE nafi TO admin;
```

Настройте параметры подключения к базе данных в файле `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nafi',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Шаг 5: Применение миграций и загрузка данных

Примените миграции для настройки базы данных:

```bash
python manage.py makemigrations
python manage.py migrate
```

Загрузите начальные данные из файла `initial_data.json`:

```bash
python manage.py loaddata initial_data.json
```

### Шаг 6: Запуск проекта

Запустите сервер разработки:

```bash
python manage.py runserver
```

Теперь проект доступен по адресу `http://127.0.0.1:8000`.

## Дополнительные команды

### Создание суперпользователя

Для доступа к административной панели создайте суперпользователя:

```bash
python manage.py createsuperuser
```

### Тестирование

Запустите тесты, чтобы убедиться, что все работает правильно:

```bash
python manage.py test
```

### Деплой на продакшн

Для деплоя на продакшн сервер настройте `settings.py` соответствующим образом (например, настройте ALLOWED_HOSTS, DEBUG и другие параметры безопасности).

## Структура проекта

- `users/` - приложение для управления пользователями и профилями.
- `meetings/` - приложение для создания и управления встречами.
- `notifications/` - приложение для управления уведомлениями.
- `courses/` - приложение для управления курсами и прогрессом пользователей.

## Лицензия

Этот проект "лицензирован" под лицензией MIT.

```

Этот README файл включает все необходимые шаги для установки и запуска проекта, а также дополнительную информацию о структуре проекта и его лицензии. Вы можете настроить его под свои конкретные нужды и добавить любую другую информацию, которая может быть полезна для пользователей вашего проекта.
```
