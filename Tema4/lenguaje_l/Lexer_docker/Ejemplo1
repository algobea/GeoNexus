# Ejemplo 1: Dockerfile basico para una aplicacion Python
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8000
CMD ["python3", "app.py"]

