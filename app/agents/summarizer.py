class Summarizer:
    def summarize(self, texts: list[str]) -> str:
        combined = " ".join(texts)
        # Truncate for demo purposes
        if len(combined) > 200:
            return combined[:200] + "..."
        return combined