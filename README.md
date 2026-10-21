# Calculator API

Осетров Степан, РИ-431003

REST API-калькулятор на Python и FastAPI.

## Версия 0.2.0

Добавлены автоматические проверки безопасности в CI/CD-пайплайн с использованием Semgrep, Trivy и Gitleaks.

## Возможности

- Сложение, вычитание, умножение и деление.
- Проверка работоспособности через `/health`.
- Обработка деления на ноль с HTTP 400.

## Технологии

- Python 3.12, FastAPI, Uvicorn
- Docker
- GitHub Actions
- GitHub Container Registry (GHCR)
- Semgrep, Trivy, Gitleaks

## API

| Метод | Endpoint | Назначение |
|---|---|---|
| GET | `/` | Информация о приложении и версии |
| GET | `/health` | Проверка работоспособности |
| POST | `/add` | Сложение |
| POST | `/subtract` | Вычитание |
| POST | `/multiply` | Умножение |
| POST | `/divide` | Деление |

Пример запроса:

```bash
curl -X POST http://127.0.0.1:8000/add \
  -H "Content-Type: application/json" \
  -d '{"a": 40, "b": 3}'
```

Ответ:

```json
{"result": 43}
```

## Запуск в Docker

```bash
docker build --build-arg APP_VERSION=0.2.0 -t calculator-api:0.2.0 .
docker run -d --name calculator-api -p 8000:8000 calculator-api:0.2.0
```

Проверка:

```bash
curl http://127.0.0.1:8000/health
```

## CI/CD и безопасность

При `push` в ветку `main` GitHub Actions:

1. Определяет версию приложения.
2. Запускает Semgrep для статического анализа исходного кода.
3. Собирает Docker-образ и проверяет его с помощью Trivy.
4. Использует Gitleaks для поиска секретов в репозитории.
5. Публикует Docker-образ в GitHub Container Registry.
6. Сохраняет автоматически увеличенную PATCH-версию в `version.env`.

Проверки безопасности формируют результаты, которые можно изучить в GitHub Actions. Найденные проблемы не во всех случаях блокируют публикацию образа.

Версия хранится в `version.env`:

```env
MAJOR=0
MINOR=2
PATCH=0
```

При обычном `push` PATCH автоматически увеличивается на единицу. При изменении MINOR или MAJOR вручную PATCH сбрасывается в `0`.

Опубликованный образ:

```text
ghcr.io/sosetrov/calculator-api
```

## Лицензия

Проект создан в учебных целях.
