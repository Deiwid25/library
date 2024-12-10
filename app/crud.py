from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from typing import Optional
from .models import Book

# Function to create a book
def create_book(db: Session, title: str, author: str, year: int, isbn: str):
    # Check if the ISBN already exists in the database
    existing_book = db.query(Book).filter(Book.isbn == isbn).first()
    if existing_book:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The ISBN is already registered in the database."
        )

    # Create a new book
    new_book = Book(title=title, author=author, year=year, isbn=isbn)

    try:
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error adding the book. The ISBN may already exist."
        )

# Function to get books with pagination
def get_books(db: Session, skip: int = 0, limit: int = 10, title: Optional[str] = None, author: Optional[str] = None):
    query = db.query(Book)
    
    # Filters by title and author (if provided)
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    
    # Apply pagination
    return query.offset(skip).limit(limit).all()

# Function to get a book by its ID
def get_book_by_id(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found."
        )
    return book

# Function to update a book
def update_book(db: Session, book_id: int, title: str, author: str, year: int, isbn: str):
    # Check if the book exists
    book_to_update = db.query(Book).filter(Book.id == book_id).first()
    if not book_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The book is not in the database."
        )
    
    # Check if the ISBN already exists (except for the book being updated)
    existing_isbn = db.query(Book).filter(Book.isbn == isbn).filter(Book.id != book_id).first()
    if existing_isbn:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The ISBN is already registered in the database."
        )

    # Update the values
    book_to_update.title = title
    book_to_update.author = author
    book_to_update.year = year
    book_to_update.isbn = isbn

    try:
        db.commit()
        db.refresh(book_to_update)
        return book_to_update
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error updating the book. The ISBN may already exist."
        )

# Function to delete a book
def delete_book(db: Session, book_id: int):
    # Find the book by ID
    book_to_delete = db.query(Book).filter(Book.id == book_id).first()
    if not book_to_delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found."
        )
    
    # Delete the book
    db.delete(book_to_delete)
    db.commit()
    return {"message": "Book successfully deleted."}
