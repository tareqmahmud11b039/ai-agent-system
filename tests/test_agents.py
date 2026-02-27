import pytest
from app.agents.retriever import Retriever
from app.agents.summarizer import Summarizer
from app.agents.orchestrator import Orchestrator

def test_retriever():
    retriever = Retriever()
    result = retriever.retrieve("ai")
    assert len(result) > 0
    assert "artificial intelligence" in result[0].lower()

def test_summarizer():
    summarizer = Summarizer()
    texts = ["First sentence.", "Second sentence."]
    summary = summarizer.summarize(texts)
    assert summary == "First sentence. Second sentence."

def test_orchestrator():
    orch = Orchestrator()
    result = orch.process_query("docker")
    assert result["query"] == "docker"
    assert len(result["retrieved_texts"]) > 0
    assert "container" in result["summary"].lower()