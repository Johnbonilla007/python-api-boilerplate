import webbrowser
import threading
from fastapi import FastAPI  # type: ignore
import uvicorn  # type: ignore
from app.services.user_service import UserService
from app.services.user_service import UserService
from app.services.core.base_app_service import BaseAppService
from app.routes.users_routes import UserRouter

app = FastAPI(
    title="Mi API con FastAPI",
    description="Esta API es un ejemplo de cómo usar FastAPI con Swagger.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json")

@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI está funcionando con Swagger!"}


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

base_service = BaseAppService()
user_service = UserService(base_service.db)
user_router = UserRouter(user_service).router

# Incluir el router de usuarios
app.include_router(user_router)

def open_browser():
    webbrowser.open("http://127.0.0.1:8000/docs")

if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()  # Espera 1.5 segundos y abre el navegador
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
