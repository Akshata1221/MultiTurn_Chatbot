from langchain_ollama import OllamaLLM

# Connect to the local Ollama model
try:
    llm = OllamaLLM(model="llama3")
except Exception:
    llm = None


def get_response(prompt):
    """Get a complete response from the LLM."""
    if llm is None:
        return "⚠️ Could not connect to Ollama. Please make sure Ollama is running (`ollama serve`)."
    try:
        response = llm.invoke(prompt)
        return response
    except Exception as e:
        return f"⚠️ Error generating response: {str(e)}"


def get_response_stream(prompt):
    """Stream response tokens from the LLM as a generator."""
    if llm is None:
        yield "⚠️ Could not connect to Ollama. Please make sure Ollama is running (`ollama serve`)."
        return
    try:
        for chunk in llm.stream(prompt):
            text = str(chunk)
            if text:
                yield text
    except Exception as e:
        yield f"\n\n⚠️ Error during streaming: {str(e)}"