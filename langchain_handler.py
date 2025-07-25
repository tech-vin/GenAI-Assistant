from langchain_community.llms import Ollama
from utils import save_memory, fetch_memory

llm = Ollama(model="llama3")

def process_prompt(prompt):
    memory = fetch_memory()

    full_prompt = f"""
    You are a resume assistant. User's saved data is: {memory} 
    User said: "{prompt}" 
    Answer appropriately. If the messafe contains new personal info. acknowledge and store.
    """
    response =llm.invoke(full_prompt)
    save_memory(prompt, response)
    return response
