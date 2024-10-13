FROM python:3.10-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install fastapi[standard]
COPY . .
CMD ["fastapi", "run", "example.py", "--host=0.0.0.0", "--port=8000", "--root-path=/restapi"]