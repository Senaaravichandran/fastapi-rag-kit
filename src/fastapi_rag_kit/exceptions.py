"""Custom exceptions for fastapi_rag_kit."""

from __future__ import annotations


class FastapiRagKitError(Exception):
    """Base exception for all FastapiRagKit errors.

    Attributes:
        message: Human-readable error description.
        code: Optional machine-readable error code.
    """

    def __init__(self, message: str, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code


class ConfigurationError(FastapiRagKitError):
    """Raised when the SDK is misconfigured."""


class ValidationError(FastapiRagKitError):
    """Raised when input validation fails."""


class TimeoutError(FastapiRagKitError):
    """Raised when an operation exceeds its time limit."""
