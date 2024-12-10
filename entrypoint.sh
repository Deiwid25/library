#!/bin/bash

# Ejecutar las pruebas con SQLite en memoria (modo de pruebas)
echo "Running tests..."
export TEST_ENV=true  # Usar SQLite en memoria para las pruebas 
pytest --maxfail=1 --disable-warnings -q

# Verificar si las pruebas pasaron
if [ $? -eq 0 ]; then
  echo "Tests passed. Starting the app..."
  # Ejecutar las migraciones de Alembic y luego iniciar la aplicación
  export TEST_ENV=false 
  alembic upgrade head
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
else
  echo "Tests failed. Exiting..."
  exit 1
fi
