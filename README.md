# 🚦 Smart Router Kit

**Part 2 of the "Smart Ingest" Series.**
(Check out Part 1: [Smart Ingest Kit](https://github.com/2dogsandanerd/smart-ingest-kit)

This kit demonstrates how to implement an **"Ingestion Traffic Controller"** for RAG systems.
Instead of blindly chunking and embedding every document, we use a small LLM pass to route documents to the correct semantic collection and choose the optimal processing strategy.

## The Problem
"Garbage In, Garbage Out."
If you mix financial tables, Python code, and general marketing text in one vector collection, your retrieval quality suffers.

## The Solution
A **Pydantic-structured decision step** before ingestion.

## Usage

1. Install dependencies:
   ```bash
   pip install pydantic
   ```

2. Run the demo:
   ```bash
   python examples/demo_routing.py
   ```

## The Core Logic (Pydantic)

```python
class RoutingDecision(BaseModel):
    target_collection: str  # e.g. 'finance', 'tech'
    chunking_strategy: Literal["standard", "table_aware", "vision"]
    confidence: float
    reasoning: str
```

## Integration
In a real setup, you would connect `DocumentRouter` to your Ollama or OpenAI client.
