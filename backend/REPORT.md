## Ответы на задание 1:
1. Что делает `backend/app_main.py`?

    - Запускает функцию `create_app()`.


2. Что делает функция `create_app()`?

    - Эта функция создает и конфигурирует `FastAIP`


3. Где объявлен endpoint `GET /health`?

    - `GET /health` объявлен в `src /bootstrap /routers.py`


4. Какая Python-функция обрабатывает `GET /health`?

    - `GET /health` обрабатывает функция `register_utility_routes(app: FastAPI)`
которая находится в `src /bootstrap /routers.py`


5. Какой JSON должен вернуть `GET /health`?

    - `GET /health` записывает в JSON при запуске FastAPI информацию о состояние API, а именно:
`"status": "ok"`

---

## Ответы на задание 2:

Команда, которую я запускал:
```bash
python -m pytest -q >> cd backend
```

Вывод результата: `100%` and `2 passed`, за время: `0.77`s

---

## Ответы на задание 3:

Команда для запуска: 
```bash
 python -m pytest backend/tests/test_health_endpoint.py -v
```
Вывод программы теста:
`backend/tests/test_health_endpoint.py::test_health_endpoint_returns_ok PASSED`

---

## Ответ на задание 4:

Команда для запуска:
```bash
uvicorn backend.app_main:app --reload
```

Страница: http://127.0.0.1:8000

Вывод страници:

`
{`

`
  "status": "ok",`

`
  "service": "python-backend-trainee-task",`

`
  "base_url": "http://127.0.0.1:8000/"`

`
}
`

---

## Отчет:

1. Написать код для в `backend\tests\test_version_endpoint.py`
   
   - Освоил создание файлов с расширением `.md` (первый раз работаю с ним)


2. Список всех команд, которые я запускал:

```bash
cd backend
python -m pytest -q
```
```bash
cd backend/tests/
```
```bash
python -m pytest backend/tests/ -v
```
```bash
uvicorn backend.app_main:app --reload

```

3. Все тесты были пройдены.


4. - `2 passed, 1 warning` было не очень понятно при первом запуске.

   - также, была ошибка с запуском оманды `uvicorn backend.app_main:app --reload`

   - была ошибка в `routers.py`, не было ` @app.get("/health", tags=["health"])`, 
перепутал в `test_health_endpoint.py` вместо `assert response.json() == {"status": "ok"}`, 
написал `assert response.json() == {
        "service": "python-backend-trainee-task",
        "version": "0.1.0",
    }
`


5. Пока не очень знаю что можно еще улучшить, т.к. как не знаю основную цель проекта.