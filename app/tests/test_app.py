import pytest


import sys
import os
import subprocess

# Añadir el directorio raíz del proyecto al path de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.main import app  # Importar la aplicación FastAPI

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from app.database import Base, get_db
from app.models import Book

# Configuración para la base de datos en memoria para las pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Inicializar Faker
fake = Faker()

# Crear una base de datos limpia para cada prueba
@pytest.fixture(scope="function")
def db():
    # Crear todas las tablas en la base de datos de prueba antes de cada prueba
    Base.metadata.create_all(bind=engine)
    db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    try:
        yield db_session
    finally:
        # Eliminar todas las tablas después de la prueba
        db_session.close()
        Base.metadata.drop_all(bind=engine)

# Test para crear un libro
def test_create_book(db):
    book_data = {
        "title": fake.sentence(nb_words=3),
        "author": fake.name(),
        "year": int(fake.year()),  # Convertir el año a entero
        "isbn": fake.isbn13()
    }

    # Simulamos la creación del libro usando la sesión de prueba
    new_book = Book(**book_data)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    # Verificamos que el libro fue creado
    assert new_book.title == book_data["title"]
    assert new_book.author == book_data["author"]
    assert new_book.year == book_data["year"]
    assert new_book.isbn == book_data["isbn"]

# Test para obtener libros
def test_get_books(db):
    # Crear datos de libro con Faker
    book_data = {
        "title": fake.sentence(nb_words=3),
        "author": fake.name(),
        "year": int(fake.year()),  # Convertir el año a entero
        "isbn": fake.isbn13()
    }
    new_book = Book(**book_data)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    # Consultar todos los libros en la base de datos
    books = db.query(Book).all()

    # Verificar que el libro esté en la base de datos
    assert len(books) == 1
    assert books[0].title == book_data["title"]
    assert books[0].author == book_data["author"]
    assert books[0].year == book_data["year"]
    assert books[0].isbn == book_data["isbn"]
