from fastapi import FastAPI
from .models import QueryRequest, QueryResponse
from .agents.orchestrator import Orchestrator

app = FastAPI(title="Multi-Agent System", description="AI agents for query processing")

orchestrator = Orchestrator()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    result = orchestrator.process_query(request.query)
    return result