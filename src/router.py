import json
from typing import Optional
from .models import RoutingDecision, FilePreview
from .prompts import ROUTER_SYSTEM_PROMPT

class DocumentRouter:
    """
    The Traffic Controller logic.
    Uses an LLM to route documents to the correct collection and strategy.
    """
    
    def __init__(self, llm_client=None):
        """
        Initialize with an LLM client.
        In a real scenario, this would be your Ollama/OpenAI client.
        """
        self.llm_client = llm_client

    def route(self, preview: FilePreview) -> RoutingDecision:
        """
        Analyzes the file preview and returns a routing decision.
        """
        # Construct the prompt
        user_message = f"Filename: {preview.filename}\n\nContent Preview:\n{preview.preview_text}"
        
        # Mocking the LLM call for this kit demonstration
        # In production, you would call: response = self.llm_client.chat(...)
        print(f"🤖 Analyzing '{preview.filename}' with Traffic Controller...")
        
        # Simulate intelligent routing based on keywords (for demo purposes)
        text_lower = preview.preview_text.lower()
        
        if "invoice" in text_lower or "total" in text_lower or "eur" in text_lower:
            return RoutingDecision(
                target_collection="finance",
                chunking_strategy="table_aware",
                requires_vision=False,
                confidence=0.95,
                reasoning="Detected financial keywords (invoice, total, currency)."
            )
        elif "def " in text_lower or "class " in text_lower or "api" in text_lower:
             return RoutingDecision(
                target_collection="technical_docs",
                chunking_strategy="standard",
                requires_vision=False,
                confidence=0.88,
                reasoning="Detected code or API documentation patterns."
            )
        elif "chart" in text_lower or "figure" in text_lower:
             return RoutingDecision(
                target_collection="general",
                chunking_strategy="vision_intensive",
                requires_vision=True,
                confidence=0.85,
                reasoning="Text implies visual content (charts/figures)."
            )
        else:
            return RoutingDecision(
                target_collection="general",
                chunking_strategy="standard",
                requires_vision=False,
                confidence=0.60,
                reasoning="No specific domain patterns detected, defaulting to general."
            )
