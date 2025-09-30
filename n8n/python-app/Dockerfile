FROM python:3.11-slim

WORKDIR /app
RUN apt-get -y update && apt-get -y install curl
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install fastapi[standard]
COPY main.py .

CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000"]
