from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from app.crud import create_book
from app.schemas import *
from app.database import get_db

router = APIRouter()

@router.post("/books/", response_model=BookResponse)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
  book_data = book.dict()
  print(book_data)
  return create_book(db, book_data)