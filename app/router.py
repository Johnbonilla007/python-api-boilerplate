from fastapi import APIRouter
from app.routes.users_routes import user_router

def create_router() -> APIRouter:
    router = APIRouter()
    router.include_router(user_router)
    return router