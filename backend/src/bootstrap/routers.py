"""HTTP routes for the trainee sandbox app."""

from fastapi import FastAPI, Request


def register_utility_routes(app: FastAPI) -> None:
    """Register simple utility endpoints."""

    @app.get("/", tags=["root"])
    async def root(request: Request) -> dict[str, str]:
        return {
            "status": "ok",
            "service": "python-backend-trainee-task",
            "base_url": str(request.base_url),
        }


    @app.get("/version", tags=["version"])
    async def version() -> dict[str, str]:
        return {
            "status": "ok",
            "service": "python-main-trainee-task",
            "version": "0.1.0",
        }
