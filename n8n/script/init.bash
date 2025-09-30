#!/bin/bash

# Start Ollama in the background
ollama serve &

# Wait until the server is ready
sleep 5


# Pull model
ollama pull llama3.2

# Wait for background server to stay in foreground
wait
