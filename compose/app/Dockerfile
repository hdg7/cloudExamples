FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install fastapi[standard]
COPY . .
CMD ["fastapi", "run", "main.py", "--host=0.0.0.0", "--port=8888"]

