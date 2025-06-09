# Use the official Debian image as the base image
FROM debian:latest

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    procps \
    wget \
    curl \
    git	\
    python3 \
    python3-pip \
    sudo \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN pip install --break-system-packages -r requirements.txt
RUN pip install --break-system-packages fastapi[standard]

WORKDIR /root
RUN mkdir models
COPY main.py .
COPY initServer.bash .
ENTRYPOINT ["bash", "initServer.bash"]