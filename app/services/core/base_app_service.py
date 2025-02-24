from sqlalchemy.orm import Session
from app.infrastructure.database import SessionLocal

class BaseAppService:
    def __init__(self, db: Session = None):
        self.db = db or SessionLocal()

    def close_db(self):
        self.db.close()
