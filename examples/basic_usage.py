#!/usr/bin/env python3
"""Basic usage example for fastapi_rag_kit."""

from fastapi_rag_kit import FastapiRagKit, FastapiRagKitOptions


def main() -> None:
    # Create with default options
    instance = FastapiRagKit()
    result = instance.run()
    print(f"Default run: success={result.success}, data={result.data}")

    # Create with custom options
    options = FastapiRagKitOptions(verbose=True)
    instance = FastapiRagKit(options)
    result = instance.run()
    print(f"Verbose run: success={result.success}, data={result.data}")


if __name__ == "__main__":
    main()
