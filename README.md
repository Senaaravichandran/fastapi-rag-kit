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
