from fastapi import FastAPI

app = FastAPI()



books = [
  {"id": 1, "tittle": "el Quijote", "author": "Miguel de cervantes", "year": 1605, "isbn": "789-908"},
  {"id": 2, "tittle": "cien años de soledad", "author": "Gabriel Garcia", "year": 1980, "isbn": "789-901"},
  {"id": 3, "tittle": "el coronel no tiene quien le escriba", "author": "Gabriel Garcia", "year": 1970 , "isbn": "789-909"},
]
@app.get("/")
def read_root():
  return{"message": "servidor en funcionamiento!"}

@app.get("/books")
def list_books():
  return{"books": books}