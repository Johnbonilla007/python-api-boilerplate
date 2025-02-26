from sqlalchemy.orm import Session
from app.infrastructure.database import SessionLocal

class BaseAppService:
    """
    Clase base para los servicios de la aplicación.

    Esta clase proporciona una sesión de base de datos y métodos comunes
    para los servicios de la aplicación.
    """

    def __init__(self, db: Session = None):
        """
        Inicializa una instancia de BaseAppService.

        Args:
            db (Session, optional): Una sesión de base de datos SQLAlchemy. Si no se proporciona,
                                    se creará una nueva sesión utilizando SessionLocal.
        """
        self.db = db or SessionLocal()

    def close_db(self):
        """
        Cierra la sesión de base de datos.

        Este método debe ser llamado para cerrar la sesión de base de datos
        cuando ya no sea necesaria.
        """
        self.db.close()