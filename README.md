# Calculator API
Осетров Степан РИ-431003
REST API калькулятор на Python и FastAPI.

## Возможности

API поддерживает следующие операции:

- сложение;
- вычитание;
- умножение;
- деление.

Также реализован endpoint `/health` для проверки работоспособности приложения.

## Запуск без Docker

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
# calculator-api
