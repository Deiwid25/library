from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import Book
from fastapi import HTTPException, status
from typing import Optional

def create_book(db: Session, book_data: dict):
    try:
        db_book = Book(**book_data)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error: There was an issue with the book data (e.g., duplicate ISBN)."
        )

def delete_book(db: Session, book_id: int):
    try:
        db_book = db.query(Book).filter(Book.id == book_id).first()
        if db_book:
            db.delete(db_book)
            db.commit()
            return db_book
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error: Book not found."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error: {str(e)}"
        )

def update_book(db: Session, book_id: int, book_data: dict):
    try:
        db_book = db.query(Book).filter(Book.id == book_id).first()
        if db_book:
            for key, value in book_data.items():
                setattr(db_book, key, value)
            db.commit()
            db.refresh(db_book)
            return db_book
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error: Book not found."
        )
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error: There was an issue with the book data (e.g., duplicate ISBN)."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error: {str(e)}"
        )

def get_books(db: Session, skip: int = 0, limit: int = 10, title: Optional[str] = None, author: Optional[str] = None):
    try:
        query = db.query(Book)
        if title:
            query = query.filter(Book.title.ilike(f"%{title}%"))
        if author:
            query = query.filter(Book.author.ilike(f"%{author}%"))

        return query.offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error: {str(e)}"
        )
