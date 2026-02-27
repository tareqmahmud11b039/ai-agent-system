# Multi-Agent System with FastAPI

This project implements a multi-agent system consisting of three agents:
- **Retriever**: Fetches relevant information from a mock knowledge base based on a user query.
- **Summarizer**: Combines and optionally truncates the retrieved texts.
- **Orchestrator**: Coordinates the workflow by calling the Retriever and then the Summarizer.

The system is exposed via a FastAPI application with two endpoints:
- `GET /health` – health check.
- `POST /query` – accepts a JSON `{"query": "..."}` and returns the processed result.

## Setup and Run

### Local (without Docker)
1. Clone the repository and navigate into the folder.
2. Create a virtual environment (optional) and install dependencies:
   ```bash
   pip install -r requirements.txt