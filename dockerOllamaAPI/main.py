from fastapi import FastAPI
import ollama
import json
app = FastAPI()

@app.post("/pull")
async def pull(model: str = 'llama3.2'):
    try:
        ollama.pull(model)
        return {"status": "success", "model": model}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

@app.post("/run")
async def run(model: str = 'llama3.2', text: str = ''):
    ollama_output = ollama.chat(
        model=model, messages= [
        {
            'role': 'user',
            'content': text,
        },
    ])
    print(ollama_output['message']['content'])
    try:
        # First ensure it's JSON-serializable (optional unless manipulation needed)
        ollama_output_json = json.dumps(ollama_output['message']['content'], ensure_ascii=False)
        ollama_output = json.loads(ollama_output_json)
    except (TypeError, json.JSONDecodeError) as e:
        print("Error handling Ollama output as JSON:", e)
        return {"status": "error", "message": "Failed to decode JSON from Ollama output"}
    if not ollama_output:
        return {"status": "error", "message": "Ollama output is empty"}
    return {"status": "success", "output": ollama_output}

