from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserDto, UserCreateDto, UserUpdateDto
from app.services.user_service import UserService
from app.services.core.base_app_service import BaseAppService

class UserRouter:
    def __init__(self, user_service: UserService):
        self.router = APIRouter(prefix="/users", tags=["Users"])
        self.user_service = user_service

        self.router.post("/", response_model=UserDto)(self.create_user)
        self.router.get("/{user_id}", response_model=UserDto)(self.read_user)
        self.router.get("/all-users", response_model=UserDto)(self.get_users)
        self.router.put("/{user_id}", response_model=UserDto)(self.update_user)
        self.router.delete("/{user_id}", response_model=UserDto)(self.delete_user)

    def create_user(self, user: UserCreateDto):
        return self.user_service.create_user(user)

    def read_user(self, user_id: int):
        db_user = self.user_service.get_user(user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user

    def get_users(self):
        db_user = self.user_service.get_users()
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user

    def update_user(self, user_id: int, user: UserUpdateDto):
        return self.user_service.update_user(user_id, user)

    def delete_user(self, user_id: int):
        return self.user_service.delete_user(user_id)

# Instanciar UserService y pasar al router
base_service = BaseAppService()  # Aquí deberías pasar la sesión de la DB si es necesario
user_service = UserService(base_service.db)
user_router = UserRouter(user_service).router
