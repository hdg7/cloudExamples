#!/bin/bash

# This script is used to run the tinyllama server in a docker container

# Check if ollama is running
ps cax | grep ollama > /dev/null
if [ $? -eq 0 ]; then
	echo "Ollama is already running"
else
	echo "Starting ollama"
	ollama serve &
	sleep 5
fi


if [ "$1" == "pull" ]; then
	echo "Running in dev mode"
	ollama pull tinyllama
elif [ "$1" == "run" ]; then
	echo "Running in prod mode"
	ollama run tinyllama
else
	echo "Invalid command"
fi

```
```
