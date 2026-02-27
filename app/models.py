from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query: str
    retrieved_texts: list[str]
    summary: str