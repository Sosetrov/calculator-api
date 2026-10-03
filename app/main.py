import os
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


def get_app_version():
    env_version = os.getenv("APP_VERSION")

    if env_version:
        return env_version

    version_file = Path(__file__).resolve().parent.parent / "version.env"

    version_data = {}

    with open(version_file, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = line.split("=", 1)
            version_data[key.strip()] = value.strip()

    return (
        f"{version_data['MAJOR']}."
        f"{version_data['MINOR']}."
        f"{version_data['PATCH']}"
    )


APP_VERSION = get_app_version()

app = FastAPI(
    title="API-Calculator by Osetrov Stepan",
    description="REST API калькулятор для задания по дисциплине Методы Оценки Безопасности Компьютерных Систем\nВыполнил Осетров Степан, РИ-431003\nПреподаватель: Крамаренко Павел Владимирович",
    version=APP_VERSION
)


class Calculation(BaseModel):
    a: float
    b: float


@app.get("/")
def root():
    return {
        "name": "API-Calc Osetrov",
        "version": APP_VERSION,
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/add")
def add(data: Calculation):
    return {"result": data.a + data.b}


@app.post("/subtract")
def subtract(data: Calculation):
    return {"result": data.a - data.b}


@app.post("/multiply")
def multiply(data: Calculation):
    return {"result": data.a * data.b}


@app.post("/divide")
def divide(data: Calculation):
    if data.b == 0:
        raise HTTPException(
            status_code=400,
            detail="Division by zero is not allowed/Запрещено деление на 0"
        )

    return {"result": data.a / data.b}
