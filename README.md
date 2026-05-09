# fastapi_rag_kit

Drop-in FastAPI utilities for RAG endpoints with citations, caching, and eval hooks.

## Installation

```bash
pip install fastapi_rag_kit
```

## Quick Start

```python
from fastapi_rag_kit import FastapiRagKit

instance = FastapiRagKit()
result = instance.run()
print(result)
```

## Features

- Pydantic models for RAG requests, citations, and tool results
- Streaming SSE responses with standardized chunk schema
- Pluggable retriever interface (FAISS/Chroma/http) with caching
- Built-in tracing hooks for prompt, context, and latency
- Minimal eval harness: golden-set checks for groundedness and citation coverage

## API Reference

### Streaming SSE Responses

`RagSSEChunk` is a Pydantic model for standardized streaming Server-Sent Events (SSE) responses in RAG endpoints. Use it to structure each chunk of your streaming response, including answer fragments, citations, tool results, and errors.

#### Example Usage

```python
from fastapi_rag_kit import RagSSEChunk, Citation

# Create a chunk for an answer fragment
chunk = RagSSEChunk(
    event="answer_fragment",
    data="Paris is the capital of France.",
    citations=[Citation(source_id="doc-1")],
    tool_results=[],
    meta={"chunk": 1}
)

# Example FastAPI streaming endpoint
from fastapi import FastAPI
from fastapi.responses import EventSourceResponse

app = FastAPI()

@app.get("/rag/stream")
def stream_rag():
    def event_generator():
        yield chunk.json()
        yield RagSSEChunk(event="done").json()
    return EventSourceResponse(event_generator())
```

See the `RagSSEChunk` docstring for all event types and fields.


### Citations and Tool Results

`Citation` and `ToolResult` are Pydantic models for representing document citations and tool/function call results in RAG pipelines. Use them to provide transparency and traceability in your RAG responses.

#### Citation Example

```python
from fastapi_rag_kit import Citation

citation = Citation(
    source_id="doc-123",
    start_char=10,
    end_char=50,
    uri="https://example.com/doc-123",
    meta={"title": "Example Doc"}
)
```

#### ToolResult Example

```python
from fastapi_rag_kit import ToolResult

result = ToolResult(
    name="summarize",
    input={"text": "Paris is the capital of France."},
    output={"summary": "Paris is France's capital."},
    success=True
)
```

You can include lists of `Citation` and `ToolResult` in your RAG responses or streaming chunks:

```python
from fastapi_rag_kit import RagResponse

response = RagResponse(
    answer="Paris is the capital of France.",
    citations=[citation],
    tool_results=[result]
)
```

See the `Citation` and `ToolResult` docstrings for all available fields and validation rules.


### `FastapiRagKit`

#### Constructor

```python
FastapiRagKit(options: FastapiRagKitOptions | None = None)
```

#### Methods

- `run()` - Execute the main operation. Returns `FastapiRagKitResult`.

## Development

```bash
# Install with dev dependencies
make install

# Run tests
make test

# Lint and type-check
make lint

# Format code
make format

# Build
make build
```

## Publishing

1. Update version in `pyproject.toml` and `src/fastapi_rag_kit/__init__.py`
2. Create a GitHub release with tag `v0.x.0`
3. The GitHub Action will automatically publish to PyPI

## License

MIT
