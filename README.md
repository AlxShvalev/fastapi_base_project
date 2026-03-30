# Шаблон веб-сервиса на FastAPI
Этот шаблон предназначен для быстрого создания веб-сервиса на FastAPI.
Он включает в себя базовую структуру проекта, а также работу с авторизацией и аутентификацией пользоватлеей.

## Технологии
- FastAPI
- Pydantic
- SQLAlchemy
- FastAPI Users
- Uvicorn
- Redis
- Poetry
- Docker
- Docker Compose

## Установка и запуск
1. Клонируйте репозиторий:
```bash
git clone
cd base_fastapi_project
```
2. Установите зависимости:
```bash
poetry install
```
3. Поднимите сервисы Redis и PostgreSQL с помощью Docker Compose:
```bash
docker-compose up -d
```
4. Запустите сервис:
```bash
poetry run uvicorn app.main:app --reload
```
