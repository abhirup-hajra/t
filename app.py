from fastapi import FastAPI

app = FastAPI(title="Deplexo API starter", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def index():
    return {"message": "Hello from Deplexo", "docs": "/docs"}
