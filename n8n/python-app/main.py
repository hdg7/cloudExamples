from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

OLLAMA_URL = "http://ollama:11434/api/generate"

@app.post("/generate")
async def generate(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "Hello, Ollama!")
        print(f"Received prompt: {prompt}")
        response = requests.post(OLLAMA_URL, json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False 
        })
        print(f"Received response: {response}")
        response.raise_for_status()
        return JSONResponse(content=response.json())
    except requests.RequestException as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": "An unexpected error occurred: " + str(e)})
