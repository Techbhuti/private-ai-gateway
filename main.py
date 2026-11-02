from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
import os

app = FastAPI(
    title="Local AIaaS Platform",
    description="A lightweight AI-as-a-Service inference and monitoring gateway.",
    version="1.0.0"
)

# Request body schema validation
class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

# Response body schema
class AIResponse(BaseModel):
    success: bool
    prompt_received: str
    response_text: str
    latency_ms: float
    model_used: str

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "AIaaS Gateway",
        "docs": "/docs"
    }

@app.post("/v1/generate", response_model=AIResponse)
def generate_ai_response(request: PromptRequest):
    start_time = time.time()
    
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")
    
    try:
        # --- MOCK / FREE LOCAL INFERENCE SIMULATION ---
        # In production or local execution, you can swap this block out 
        # to interface with a local llama.cpp / Ollama instance running on port 11434.
        simulated_output = f"Processed locally: '{request.prompt[:50]}...' [Execution successful]"
        
        # Calculate latency
        end_time = time.time()
        latency = round((end_time - start_time) * 1000, 2)
        
        return AIResponse(
            success=True,
            prompt_received=request.prompt,
            response_text=simulated_output,
            latency_ms=latency,
            model_used="local-lightweight-engine"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
