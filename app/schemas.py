from pydantic import BaseModel
from typing import Optional


class BookCreate(BaseModel):
  title: str
  author: str
  year: int
  isbn: str

class BookResponse(BaseModel):
  id: int
  title: str
  author: str
  year: int
  isbn: str

  class Config:
    orm_mode = True 