from fastapi import APIRouter

class BaseRouter:
    def __init__(self, prefix: str = ""):
        self.router = APIRouter(prefix=prefix)

    def get_router(self):
        return self.router