# Trial tasks

Привет! Это пробное задание на Python backend.

Не нужно делать всё идеально. Важно показать, как ты читаешь код, думаешь, запускаешь тесты и задаёшь вопросы.

---

## Правила

1. Не переписывай весь проект.
2. Не добавляй новые зависимости без причины.
3. Не меняй структуру проекта без согласования.
4. Делай маленькие изменения.
5. Если что-то не запускается — честно опиши ошибку.
6. После выполнения сделай Pull Request.

---

## Задание 1 — понять структуру

Открой файлы:

- `backend/app_main.py`
- `backend/src/bootstrap/app_factory.py`
- `backend/src/bootstrap/routers.py`

Ответь в комментарии к Pull Request или в файле `REPORT.md`:

1. Что делает `backend/app_main.py`?
2. Что делает функция `create_app()`?
3. Где объявлен endpoint `GET /health`?
4. Какая Python-функция обрабатывает `GET /health`?
5. Какой JSON должен вернуть `GET /health`?

---

## Задание 2 — запустить существующие тесты

Выполни:

```bash
cd backend
python -m pytest -q
```

В отчёте напиши:

- какую команду запускал;
- прошли тесты или нет;
- если была ошибка — скопируй короткий текст ошибки и напиши, что понял.

---

## Задание 3 — дописать тест на `/health`

Открой файл:

```text
backend/tests/test_health_endpoint.py
```

Если тест уже есть — проверь, что он понятен и проходит.

Тест должен проверять:

1. `GET /health` возвращает HTTP status `200`;
2. JSON ответа равен `{"status": "ok"}`.

Пример ожидаемой проверки:

```python
assert response.status_code == 200
assert response.json() == {"status": "ok"}
```

---

## Задание 4 — добавить новый endpoint `/version`

Добавь в `backend/src/bootstrap/routers.py` новый endpoint:

```text
GET /version
```

Он должен вернуть:

```json
{
  "service": "python-backend-trainee-task",
  "version": "0.1.0"
}
```

Требования:

1. endpoint должен быть объявлен рядом с `/health`;
2. endpoint не должен обращаться к базе данных;
3. endpoint не должен требовать авторизации;
4. нужно добавить тест в `backend/tests/test_version_endpoint.py`.

Тест должен проверять:

```python
response = client.get("/version")
assert response.status_code == 200
assert response.json() == {
    "service": "python-backend-trainee-task",
    "version": "0.1.0",
}
```

---

## Задание 5 — отчёт

Создай файл:

```text
REPORT.md
```

Ответь коротко:

1. Что получилось сделать?
2. Какие команды запускал?
3. Какие тесты прошли?
4. Что было непонятно?
5. Что бы ты улучшил в проекте, если бы было больше времени?

---

## Что должно быть в Pull Request

В PR должны быть:

- тест на `/health`, если его нужно было дописать;
- endpoint `/version`;
- тест на `/version`;
- `REPORT.md`;
- маленький понятный diff.

Не должно быть:

- `.venv/`;
- `__pycache__/`;
- `.pytest_cache/`;
- случайных больших файлов;
- секретов, паролей, токенов.
