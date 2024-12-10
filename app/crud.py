from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models import Book
from typing import Optional



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


def update_book(db: Session, book_id: int, book_data: dict):
  db_book = db.query(Book).filter(Book.id == book_id).first()
  if db_book:
    for key, value in book_data.items():
      setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book
  return None

def get_books(db: Session, skip: int = 0, limit: int = 10, title: Optional[str] = None, author: Optional[str] = None):
  query = db.query(Book)
  if title:
    query = query.filter(Book.title.ilike(f"%{title}%"))
  if author:
    query = query.filter(Book.author.ilike(f"%{author}%"))

  return query.offset(skip).limit(limit).all()