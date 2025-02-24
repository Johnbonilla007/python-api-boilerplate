from sqlalchemy import create_engine, Column, Integer, String, Index # type: ignore
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener la URL de la base de datos desde .env
DATABASE_URL = "mssql+pyodbc://(localdb)\MSSQLLocalDB/PythonDB?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes&MultipleActiveResultSets=True"

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definida en el archivo .env")

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear la fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Definir la base para los modelos
Base = declarative_base()


