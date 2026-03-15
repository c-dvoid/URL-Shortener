# URL Shortener

Простой сервис для сокращения ссылок с генерацией коротких URL.  
Используется PostgreSQL для хранения данных с поддержкой TTL (автоматическое удаление истёкших ссылок).

---

## Функционал

- Создание короткой ссылки (POST `/short_url`)
- Редирект по короткой ссылке (GET `/{slug}`)
- Автоматическое истечение ссылок через заданное количество дней

---

## Требования

- Python 3.14+
- PostgreSQL 18+
- FastAPI 0.128+
- SQLAlchemy 2.0+
- Alembic 1.0+
- Docker и Docker Compose

---

## Запуск через Docker (рекомендуется)

1. Клонируем репозиторий:
```bash
git clone https://github.com/c-dvoid/url-shortener.git
cd URL-Shortener
```

2. Создаём `.env` файл на основе примера:
```bash
# Linux / Mac
cp .env.example .env
# Windows
copy .env.example .env
```

3. При необходимости редактируем переменные в `.env`

4. Запускаем:
```bash
docker compose up --build
```

Приложение будет доступно на `http://localhost:8000`

---

## Локальный запуск (без Docker)

1. Клонируем репозиторий:
```bash
git clone https://github.com/c-dvoid/url-shortener.git
cd URL-Shortener
```

2. Создаём виртуальное окружение и устанавливаем зависимости:
```bash
python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt
```

3. Создаём `.env` файл и заполняем переменные (см. `.env.example`)

4. Применяем миграции:
```bash
alembic upgrade head
```

5. Запускаем приложение:
```bash
uvicorn app.main:app --reload
```

Приложение будет доступно на `http://localhost:8000`