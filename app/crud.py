from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models import Book

def create_book(db: Session, book_data: dict):
  db_book= Book(**book_data)
  db.add(db_book)
  db.commit()
  db.refresh(db_book)
  return db_book


def delete_book(db: Session, book_id: int):
  db_book = db.query(Book).filter(Book.id == book_id).first()
  if db_book:
    db.delete(db_book)
    db.commit()
    return db_book
  return None