from pydantic import BaseModel, Field
from typing import Literal, Optional, Dict, Any

class RoutingDecision(BaseModel):
    """
    The AI Traffic Controller's decision.
    Decides where a document belongs and how it should be processed.
    """
    target_collection: str = Field(
        ..., 
        description="The semantic domain for the document (e.g. 'finance', 'technical_docs', 'legal', 'general')"
    )
    chunking_strategy: Literal["standard", "table_aware", "vision_intensive"] = Field(
        ...,
        description="The best strategy to process this document based on its structure."
    )
    requires_vision: bool = Field(
        default=False,
        description="Whether the document contains complex visual elements (charts, diagrams) that require VLM processing."
    )
    confidence: float = Field(
        ..., 
        ge=0.0, 
        le=1.0, 
        description="Confidence score of the routing decision."
    )
    reasoning: str = Field(
        ..., 
        description="Brief explanation of why this routing decision was made."
    )

class FilePreview(BaseModel):
    """Minimal preview of a file for analysis."""
    filename: str
    preview_text: str = Field(..., description="The first ~2000 characters of the document text.")
    mime_type: str = "application/pdf"
