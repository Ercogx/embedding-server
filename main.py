from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Union
from sentence_transformers import SentenceTransformer
import uvicorn
import sys

app = FastAPI(title="Local Embedding Server (OpenAI-compatible)")

# Global variable for the model
model = None

class EmbeddingsRequest(BaseModel):
    model: str
    input: Union[str, List[str]]

def load_model():
    global model
    try:
        print("Loading model 'hkunlp/instructor-large'. This may take a few minutes...")
        model = SentenceTransformer("hkunlp/instructor-large")
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        sys.exit(1)

@app.post("/v1/embeddings")
async def get_embeddings(req: EmbeddingsRequest):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not initialized")
    
    if req.model != "instructor-large":
        raise HTTPException(status_code=400, detail="Model not supported. Use 'instructor-large'.")

    try:
        texts = [req.input] if isinstance(req.input, str) else req.input
        embeddings = model.encode(texts, normalize_embeddings=True)

        response = {
            "object": "list",
            "data": [
                {"object": "embedding", "embedding": emb.tolist(), "index": idx}
                for idx, emb in enumerate(embeddings)
            ],
            "model": "instructor-large",
            "usage": {"prompt_tokens": sum(len(t.split()) for t in texts), "total_tokens": sum(len(t.split()) for t in texts)}
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating embeddings: {str(e)}")

if __name__ == "__main__":
    load_model()  # Load model before starting the server
    uvicorn.run(app, host="0.0.0.0", port=8001)