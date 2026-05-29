"""FastAPI application factory."""

from fastapi import FastAPI

from backend.src.bootstrap.routers import register_utility_routes


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(title="Python Backend Trainee Task", version="0.1.0")

    register_utility_routes(app)

    return app
