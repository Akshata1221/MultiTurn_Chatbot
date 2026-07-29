from langchain_ollama import OllamaLLM

# Connect to the local Ollama model
llm = OllamaLLM(model="llama3")

def get_response(prompt):
    response = llm.invoke(prompt)
    return response