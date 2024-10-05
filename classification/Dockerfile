FROM python:3.9-slim-buster
RUN apt-get update && apt-get install -y gcc g++
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["jupyter" ,"notebook" , "--ip" , "0.0.0.0" , "--port" , "8888 " ,"--allow-root"]