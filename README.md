# Calculator API

Осетров Степан, РИ-431003

REST API калькулятор на Python и FastAPI.

## Версия 0.1.2

В версии `0.1.2` добавлено автоматическое версионирование приложения через GitHub Actions.

* `MAJOR` и `MINOR` задаются вручную в `version.env`;
* `PATCH` автоматически увеличивается на 1 при каждом `push`;
* Docker-образ автоматически собирается и публикуется в GitHub Container Registry.

## Возможности

* сложение;
* вычитание;
* умножение;
* деление;
* проверка работоспособности через `/health`.

## Технологии

* Python 3.12
* FastAPI
* Uvicorn
* Docker
* GitHub Actions
* GitHub Container Registry

## Структура проекта

```text
calculator-api/
├── .github/
│   └── workflows/
│       └── docker-publish.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
└── version.env
```

## API

### GET `/`

```bash
curl http://127.0.0.1:8000/
```

```json
{
  "name": "API-Calc Osetrov",
  "version": "0.1.0",
  "status": "running"
}
```

### GET `/health`

```bash
curl http://127.0.0.1:8000/health
```

```json
{
  "status": "ok"
}
```

### POST `/add`

```bash
curl -X POST http://127.0.0.1:8000/add \
  -H "Content-Type: application/json" \
  -d '{"a": 40, "b": 3}'
```

```json
{
  "result": 43
}
```

### POST `/subtract`

```bash
curl -X POST http://127.0.0.1:8000/subtract \
  -H "Content-Type: application/json" \
  -d '{"a": 54, "b": 5}'
```

```json
{
  "result": 49
}
```

### POST `/multiply`

```bash
curl -X POST http://127.0.0.1:8000/multiply \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 5}'
```

```json
{
  "result": 50
}
```

### POST `/divide`

```bash
curl -X POST http://127.0.0.1:8000/divide \
  -H "Content-Type: application/json" \
  -d '{"a": 100, "b": 25}'
```

```json
{
  "result": 4
}
```

При делении на ноль API возвращает HTTP 400:

```bash
curl -X POST http://127.0.0.1:8000/divide \
  -H "Content-Type: application/json" \
  -d '{"a": 12, "b": 0}'
```

## Запуск в Docker

Сборка:

```bash
docker build \
  --build-arg APP_VERSION=0.1.0 \
  -t calculator-api:0.1.0 .
```

Запуск:

```bash
docker run -d \
  --name calculator-api \
  -p 8000:8000 \
  calculator-api:0.1.0
```

Проверка:

```bash
curl http://127.0.0.1:8000/health
```

Логи:

```bash
docker logs calculator-api
```

## CI/CD и версионирование

Текущая версия хранится в `version.env`:

```env
MAJOR=0
MINOR=1
PATCH=0
```

При обычном `push` GitHub Actions автоматически увеличивает `PATCH`:

```text
0.1.0 → 0.1.1 → 0.1.2 → ...
```

При выпуске новой MINOR-версии изменяется:

```env
MINOR=2
PATCH=0
```

После этого версия начинается с:

```text
0.2.0 → 0.2.1 → 0.2.2 → ...
```

MAJOR-версия изменяется аналогично.

GitHub Actions автоматически:

1. определяет версию;
2. собирает Docker-образ;
3. публикует его в GitHub Container Registry;
4. обновляет `version.env`, если `PATCH` был увеличен автоматически.

Образ:

```text
ghcr.io/sosetrov/calculator-api
```

## Лицензия

Проект создан в учебных целях.
