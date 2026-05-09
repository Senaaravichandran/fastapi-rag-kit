"""Core module for fastapi_rag_kit."""

from .types import FastapiRagKitOptions, FastapiRagKitResult


class FastapiRagKit:
    """Drop-in FastAPI utilities for RAG endpoints with citations, caching, and eval hooks.

    Example::

        from fastapi_rag_kit import FastapiRagKit

        instance = FastapiRagKit()
        result = instance.run()
        print(result)
    """

    def __init__(self, options: FastapiRagKitOptions | None = None) -> None:
        self.options = options or FastapiRagKitOptions()

    def run(self) -> FastapiRagKitResult:
        """Execute the main operation.

        Returns:
            FastapiRagKitResult with the operation outcome.
        """
        # TODO: Implement core functionality
        # Key features to implement:
        #   - Pydantic models for RAG requests, citations, and tool results
        #   - Streaming SSE responses with standardized chunk schema
        #   - Pluggable retriever interface (FAISS/Chroma/http) with caching
        #   - Built-in tracing hooks for prompt, context, and latency
        #   - Minimal eval harness: golden-set checks for groundedness and citation coverage

        return FastapiRagKitResult(
            success=True,
            data={"message": "FastapiRagKit is working!"},
        )
