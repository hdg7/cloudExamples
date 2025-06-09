#!/bin/bash

# This script is used to run the tinyllama server in a docker container

# Check if ollama is running
ps cax | grep ollama > /dev/null
if [ $? -eq 0 ]; then
    echo "Ollama is already running"
else
    echo "Starting ollama"
    OLLAMA_MODELS=/root/models ollama serve 2> /dev/null &
    sleep 5
fi

#Command options
if [ "$1" == "pull" ]; then
    echo "Running in dev mode"
    ollama pull llama3.2:1b
elif [ "$1" == "run" ]; then
    echo "Running in prod mode"
    python3 main.py $2 
else
    echo "Invalid command"
fi
