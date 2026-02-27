from .retriever import Retriever
from .summarizer import Summarizer

class Orchestrator:
    def __init__(self):
        self.retriever = Retriever()
        self.summarizer = Summarizer()

    def process_query(self, query: str) -> dict:
        retrieved = self.retriever.retrieve(query)
        summary = self.summarizer.summarize(retrieved)
        return {
            "query": query,
            "retrieved_texts": retrieved,
            "summary": summary
        }