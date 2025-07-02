import requests
import json

def query_ollama(prompt, model="mistral"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt}
    )
    output = ""
    for chunk in response.iter_lines():
        if chunk:
            data = json.loads(chunk.decode())
            output += data.get("response", "")
    return output
