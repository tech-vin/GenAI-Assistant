import json
from pathlib import Path

MEMORY_FILE = Path("memory_store.json")

def fetch_memory():
    if not MEMORY_FILE.exists() or MEMORY_FILE.stat().st_size == 0:
        return {}
    
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_memory(prompt, response):
    memory = fetch_memory()
    memory[prompt] = response

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)