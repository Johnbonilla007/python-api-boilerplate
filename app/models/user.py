from sqlalchemy import Column, Integer, String, Index
from app.infrastructure.database import Base

# Modelo de usuario
class User(Base):
    __tablename__ = 'User'
    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String(255), index=False)
    Password = Column(String(255), index=False)
    Email = Column(String(255), index=False)  # Nueva columna