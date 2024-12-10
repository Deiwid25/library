from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from app.crud import create_book, delete_book, update_book, get_books
from app.schemas import *
from app.database import get_db

router = APIRouter()

@router.post("/books/", response_model=BookResponse)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
  book_data = book.model_dump()
  print(book_data)
  return create_book(db, book_data)

@router.delete("/books/{book_id}")
def delete_book_entry(book_id: int, db: Session =  Depends(get_db)):
  deleted_book = delete_book(db, book_id)
  if not deleted_book:
    raise HTTPException(status_code=404, detail="Book not found")
  return {"message": "Book delete successfully"}

@router.put("/books/{book_id}", response_model=BookResponse)
def update_book_details(book_id: int, book_data: BookCreate, db: Session = Depends(get_db)):
  updated_book = update_book(db, book_id, book_data.dict())
  if not updated_book:
    raise HTTPException(status_code=404, detail="Book not found")
  return updated_book

@router.get("/books/", response_model=list[BookResponse])
def lists_books(skip: int = 0, limit: int = 10, title: Optional[str] = None, author: Optional[str] = None,  db: Session = Depends(get_db)):
  return get_books(db, skip, limit, title=title, author=author)