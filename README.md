
# URL Shortener

Простой сервис для сокращения ссылок с генерацией коротких URL.  
Используется PostgreSQL для хранения данных с поддержкой TTL (автоматическое удаление истёкших ссылок).
Фронтенд подключён через Nginx (обслуживание статики и проксирование API).

---

## Функционал

- Создание короткой ссылки (POST `/short_url`)
- Создание короткой ссылки с кастомным slug (POST `/short_url` с полем `custom_slug`)
- Редирект по короткой ссылке (GET `/{slug}`)
- Просмотр информации о ссылке (GET `/info/{slug}`)
- Счётчик переходов по ссылке
- Автоматическое истечение ссылок через заданное количество дней

---

## Требования

- Python 3.14+
- PostgreSQL 18+
- FastAPI 0.128+
- SQLAlchemy 2.0+
- Alembic 1.0+
- Docker и Docker Compose
- Nginx (для фронтенда и проксирования API)

---

Клонируем репозиторий:

```bash
git clone https://github.com/c-dvoid/url-shortener.git
cd URL-Shortener
```

## Запуск через Docker (рекомендуется)

1. Создаём `.env` файл на основе примера:

```bash
# Linux / Mac
cp .env.example .env
# Windows
copy .env.example .env
```
2. При необходимости редактируем переменные в `.env`

3. Запускаем сервис через Docker Compose (backend + frontend + nginx):

```bash
docker compose up --build
```
Миграции применятся автоматически перед стартом приложения.
Nginx проксирует /api на FastAPI и обслуживает статику фронтенда.  
Приложение будет доступно на `http://localhost`

---

## Локальный запуск (для разработки)

1. Создаём виртуальное окружение и устанавливаем зависимости:

```bash
python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt
```
2. Создаём `.env` файл и заполняем переменные (см. `.env.example`)

3. Применяем миграции:

```bash
alembic upgrade head
```
4. Запускаем приложение:

```bash
uvicorn app.main:app --reload
```
Приложение будет доступно на `http://localhost:8000`
