# Calculator API
Осетров Степан РИ-431003
REST API калькулятор на Python и FastAPI.

## Возможности

API поддерживает:

* сложение;
* вычитание;
* умножение;
* деление;
* проверку работоспособности приложения через `/health`;

## Технологии

* Python 3.12
* FastAPI
* Uvicorn
* Docker
* Git

## Структура проекта

```text
calculator-api/
├── app/
│   ├── __init__.py
│   └── main.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

## API

### GET `/`

Возвращает информацию о приложении.

Пример запроса:

```bash
curl http://127.0.0.1:8000/
```

Пример ответа:

```json
{
  "name": "API-Calc Osetrov",
  "version": "0.0.1",
  "status": "running"
}
```

### GET `/health`

Проверяет работоспособность приложения.

```bash
curl http://127.0.0.1:8000/health
```

Ответ:

```json
{
  "status": "ok"
}
```

### POST `/add`

Сложение двух чисел.

```bash
curl -X POST http://127.0.0.1:8000/add \
  -H "Content-Type: application/json" \
  -d '{"a": 40, "b": 3}'
```

Ответ:

```json
{
  "result": 43
}
```

### POST `/subtract`

Вычитание второго числа из первого.

```bash
curl -X POST http://127.0.0.1:8000/subtract \
  -H "Content-Type: application/json" \
  -d '{"a": 54, "b": 5}'
```

Ответ:

```json
{
  "result": 49
}
```

### POST `/multiply`

Умножение двух чисел.

```bash
curl -X POST http://127.0.0.1:8000/multiply \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 5}'
```

Ответ:

```json
{
  "result": 50
}
```

### POST `/divide`

Деление первого числа на второе.

```bash
curl -X POST http://127.0.0.1:8000/divide \
  -H "Content-Type: application/json" \
  -d '{"a": 100, "b": 25}'
```

Ответ:

```json
{
  "result": 4
}
```

При попытке деления на ноль API возвращает HTTP 400:

```bash
curl -X POST http://127.0.0.1:8000/divide \
  -H "Content-Type: application/json" \
  -d '{"a": 12, "b": 0}'
```

Ответ:

```json
{
  "detail": "Division by zero is not allowed/Запрещено деление на 0"
}
```

## Запуск без Docker

### 1. Клонирование репозитория

```bash
git clone git@github.com:Sosetrov/calculator-api.git
cd calculator-api
```

### 2. Создание виртуального окружения

```bash
python3 -m venv .venv
```

Активация:

```bash
source .venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Запуск приложения

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

После запуска API доступно по адресу:

```text
http://127.0.0.1:8000
```

Для остановки приложения:

```text
Ctrl+C
```

## Запуск в Docker

### Сборка Docker-образа

```bash
docker build -t calculator-api:0.0.1 .
```

### Запуск контейнера

```bash
docker run -d \
  --name calculator-api \
  -p 8000:8000 \
  calculator-api:0.0.1
```

Проверить запущенные контейнеры:

```bash
docker ps
```

### Проверка API

```bash
curl http://127.0.0.1:8000/health
```

### Просмотр логов

```bash
docker logs calculator-api
```

Для просмотра логов в реальном времени:

```bash
docker logs -f calculator-api
```

### Остановка контейнера

```bash
docker stop calculator-api
```

### Удаление контейнера

```bash
docker rm calculator-api
```

### Удаление Docker-образа

```bash
docker rmi calculator-api:0.0.1
```

## Версионирование

Текущая версия API:

```text
0.0.1
```

Версия приложения указывается в `app/main.py`:

```python
app = FastAPI(
    title="Calculator API",
    description="REST API калькулятор",
    version="0.0.1"
)
```

Версия также используется при создании Docker-образа:

```bash
docker build -t calculator-api:0.0.1 .
```

## Проверка работоспособности

После запуска приложения можно выполнить:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/health
```

И проверить арифметические операции:

```bash
curl -X POST http://127.0.0.1:8000/add \
  -H "Content-Type: application/json" \
  -d '{"a": 11, "b": 9}'

curl -X POST http://127.0.0.1:8000/subtract \
  -H "Content-Type: application/json" \
  -d '{"a": 80, "b": 45}'

curl -X POST http://127.0.0.1:8000/multiply \
  -H "Content-Type: application/json" \
  -d '{"a": 12, "b": 12}'

curl -X POST http://127.0.0.1:8000/divide \
  -H "Content-Type: application/json" \
  -d '{"a": 130, "b": 2}'
```

## Лицензия

Проект создан в учебных целях.
