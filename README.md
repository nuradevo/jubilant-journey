# Python Backend Trainee Task

Это маленький sandbox-проект для первого знакомства с backend на Python/FastAPI.

Цель задания — не написать большую фичу, а показать, что ты умеешь:

- открыть незнакомый проект;
- понять, где создаётся FastAPI app;
- найти endpoint;
- написать маленький тест;
- запустить pytest;
- сделать commit и Pull Request.

## Что внутри

```text
backend/
├── app_main.py                    # точка входа приложения
├── src/bootstrap/app_factory.py   # create_app(), сборка FastAPI app
├── src/bootstrap/routers.py       # endpoint'ы и router'ы
└── tests/                         # тесты
```

## Как установить

Создай виртуальное окружение:

```bash
python -m venv .venv
```

Активируй его.

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Установи зависимости:

```bash
pip install -r requirements.txt
```

## Как запустить тесты

```bash
cd backend
python -m pytest -q
```

## Как запустить сервер

Из корня repo:

```bash
uvicorn backend.app_main:app --reload
```

Потом открой:

```text
http://127.0.0.1:8000/health
```

Ожидаемый ответ:

```json
{"status": "ok"}
```

## Что делать дальше

Открой файл `TASKS.md` и выполни задания по порядку.
