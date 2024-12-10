import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator

# Definir la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://library:library@db:5432/biblioteca")

# Si estamos en el entorno de prueba, usamos SQLite en memoria
if os.getenv("TEST_ENV") == "true":
    DATABASE_URL = "sqlite:///:memory:"

# Crear el motor y la sesión de SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Función para obtener una sesión de base de datos
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
