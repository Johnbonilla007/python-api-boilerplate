from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreateDto, UserUpdateDto
from app.services.core.base_app_service import BaseAppService

class UserService(BaseAppService):
    def __init__(self, db: Session):
        super().__init__(db)

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.Id == user_id).first()
    
    def get_all_users(self):
        return self.db.query(User).all()

    def get_users(self, skip: int = 0, limit: int = 10):
        return self.db.query(User).offset(skip).limit(limit).all()

    def create_user(self, user: UserCreateDto):
        db_user = User(Name=user.Name, Password=user.Password, Email=user.Email)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update_user(self, user_id: int, user: UserUpdateDto):
        db_user = self.get_user(user_id)
        if db_user:
            db_user.Name = user.Name
            db_user.Password = user.Password
            db_user.Email = user.Email
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int):
        db_user = self.get_user(user_id)
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
        return db_user
