"""Type definitions for fastapi_rag_kit."""

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class FastapiRagKitOptions:
    """Configuration options for FastapiRagKit.

    Attributes:
        verbose: Enable verbose logging for debugging.
        feature_1: Configuration for: Pydantic models for RAG requests, citations, and tool results
        feature_2: Configuration for: Streaming SSE responses with standardized chunk schema
        feature_3: Configuration for: Pluggable retriever interface (FAISS/Chroma/http) with caching
        feature_4: Configuration for: Built-in tracing hooks for prompt, context, and latency
        feature_5: Configuration for: Minimal eval harness: golden-set checks for groundedness and citation coverage
    """

    verbose: bool = False
    feature_1: Optional[dict[str, Any]] = None
    feature_2: Optional[dict[str, Any]] = None
    feature_3: Optional[dict[str, Any]] = None
    feature_4: Optional[dict[str, Any]] = None
    feature_5: Optional[dict[str, Any]] = None


@dataclass
class FastapiRagKitResult:
    """Result returned by FastapiRagKit operations.

    Attributes:
        success: Whether the operation succeeded.
        data: The result data, if successful.
        error: Error message, if the operation failed.
    """

    success: bool
    data: Any = field(default=None)
    error: Optional[str] = None
