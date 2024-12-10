FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el código fuente y el script de entrada
COPY . .

# Copiar el script de entrada y darle permisos de ejecución
RUN chmod +x entrypoint.sh

# Exponer el puerto de la aplicación
EXPOSE 8000

# Usar el script de entrada como CMD
CMD ["./entrypoint.sh"]
