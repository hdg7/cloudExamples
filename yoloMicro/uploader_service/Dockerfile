FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn aio-pika python-multipart
RUN pip install fastapi[standard]
CMD ["fastapi", "run", "main.py", "--host=0.0.0.0", "--port=8010"]

