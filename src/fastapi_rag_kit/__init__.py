"""
fastapi_rag_kit - Drop-in FastAPI utilities for RAG endpoints with citations, caching, and eval hooks.
"""

__version__ = "0.1.0"

from .pydantic_models_for_rag_reques import FastapiRagKit
from .types import FastapiRagKitOptions, FastapiRagKitResult
from .exceptions import FastapiRagKitError, ConfigurationError, ValidationError
from .rag_models import RagRequest, RagResponse, Citation, ToolResult
from .sse_models import RagSSEChunk

__all__ = [
    "FastapiRagKit",
    "FastapiRagKitOptions",
    "FastapiRagKitResult",
    "FastapiRagKitError",
    "ConfigurationError",
    "ValidationError",
    "RagRequest",
    "RagResponse",
    "Citation",
    "ToolResult",
    "RagSSEChunk",
]
