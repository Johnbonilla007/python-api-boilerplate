from sqlalchemy import Column, Integer, String
from app.infrastructure.database import Base

# Modelo de usuario
class Product(Base):
    __tablename__ = 'Product'
    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String(255), index=True)
    Description = Column(String(255), index=True)