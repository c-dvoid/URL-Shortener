
# URL Shortener

Простой сервис для сокращения ссылок с генерацией коротких URL.  
Используется SQLite через `aiosqlite` для локальной разработки.

---

## Функционал

- Создание короткой ссылки (POST `/short_url`)  
- Редирект по короткой ссылке (GET `/{slug}`)  

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

3. Запускаем приложение:
```bash
uvicorn app.main:app --reload
