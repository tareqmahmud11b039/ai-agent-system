class Retriever:
    def __init__(self):
        # Mock knowledge base
        self.knowledge_base = {
            "ai": [
                "Artificial intelligence (AI) is the simulation of human intelligence in machines.",
                "AI is used in various applications like robotics, natural language processing, and computer vision."
            ],
            "docker": [
                "Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers.",
                "Containers are isolated from each other and bundle their own software, libraries, and configuration files."
            ],
            "fastapi": [
                "FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.",
                "FastAPI automatically generates OpenAPI documentation and supports asynchronous programming."
            ]
        }

    def retrieve(self, query: str) -> list[str]:
        query_lower = query.lower()
        results = []
        for key, texts in self.knowledge_base.items():
            if key in query_lower:
                results.extend(texts)
        if not results:
            results = ["No relevant information found."]
        return results