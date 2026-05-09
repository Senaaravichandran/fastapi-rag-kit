"""
Pydantic models for RAG requests, citations, and tool results.

These models define the standard request/response schema for RAG endpoints.
"""
from typing import List, Optional, Any, Dict
from pydantic import BaseModel, Field, field_validator, model_validator, root_validator, validator
from .exceptions import ValidationError

class Citation(BaseModel):
    """
    Represents a citation for a retrieved document or passage.

    Example::
        Citation(
            source_id="doc-123",
            start_char=10,
            end_char=50,
            uri="https://example.com/doc-123",
            meta={"title": "Example Doc"}
        )
    """
    source_id: str = Field(..., description="Unique identifier for the source document.")
    start_char: Optional[int] = Field(None, description="Start character offset in the context.")
    end_char: Optional[int] = Field(None, description="End character offset in the context.")
    uri: Optional[str] = Field(None, description="Resolvable URI for the source document.")
    meta: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional metadata.")

    @field_validator('start_char', 'end_char')
    @classmethod
    def non_negative(cls, v: Optional[int], info: Any) -> Optional[int]:
        if v is not None and v < 0:
            raise ValidationError(f"{info.field_name} must be non-negative.")
        return v

class RagRequest(BaseModel):
    """
    Standard request model for a RAG endpoint.

    Example::
        RagRequest(
            query="What is the capital of France?",
            top_k=3,
            user_id="user-42"
        )
    """
    query: str = Field(..., description="User's query string.")
    top_k: int = Field(5, ge=1, le=100, description="Number of documents to retrieve.")
    user_id: Optional[str] = Field(None, description="Optional user/session identifier.")
    extra: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional request metadata.")

    @field_validator('query')
    @classmethod
    def query_not_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValidationError("Query must not be empty.")
        return v

class ToolResult(BaseModel):
    """
    Represents the result of a tool or function call in a RAG pipeline.

    Example::
        ToolResult(
            name="summarize",
            input={"text": "..."},
            output={"summary": "..."},
            success=True
        )
    """
    name: str = Field(..., description="Name of the tool/function.")
    input: Dict[str, Any] = Field(..., description="Input arguments to the tool.")
    output: Optional[Dict[str, Any]] = Field(None, description="Output/result from the tool.")
    success: bool = Field(True, description="Whether the tool execution succeeded.")
    error: Optional[str] = Field(None, description="Error message if failed.")

    @model_validator(mode="after")
    def check_success_and_error(self) -> "ToolResult":
        if self.success is False and not self.error:
            raise ValidationError("If success is False, error must be provided.")
        return self

class RagResponse(BaseModel):
    """
    Standard response model for a RAG endpoint.

    Example::
        RagResponse(
            answer="Paris is the capital of France.",
            citations=[Citation(source_id="doc-1")],
            tool_results=[ToolResult(name="search", input={}, output={})]
        )
    """
    answer: str = Field(..., description="Final answer string.")
    citations: List[Citation] = Field(default_factory=list, description="List of citations supporting the answer.")
    tool_results: List[ToolResult] = Field(default_factory=list, description="Results from tools/functions used.")
    meta: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional metadata.")
