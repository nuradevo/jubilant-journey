from fastapi import FastAPI

from backend.src.bootstrap.app_factory import create_app


def test_create_app_returns_fastapi_application() -> None:
    app = create_app()

    assert isinstance(app, FastAPI)
    assert app.title == "Python Backend Trainee Task"
