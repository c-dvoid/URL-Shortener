
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

---

## Установка и запуск

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

3. Создаём файл `.env` в корне проекта:
```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/url_shortener
```

4. Запускаем приложение:
```bash
uvicorn app.main:app --reload
```