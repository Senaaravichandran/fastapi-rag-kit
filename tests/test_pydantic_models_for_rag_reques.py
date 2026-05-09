"""Tests for fastapi_rag_kit."""

from fastapi_rag_kit import FastapiRagKit, FastapiRagKitOptions


class TestFastapiRagKit:
    def test_create_instance_with_defaults(self) -> None:
        instance = FastapiRagKit()
        assert instance is not None

    def test_create_instance_with_options(self) -> None:
        options = FastapiRagKitOptions(verbose=True)
        instance = FastapiRagKit(options)
        assert instance.options.verbose is True

    def test_run_successfully(self) -> None:
        instance = FastapiRagKit()
        result = instance.run()
        assert result.success is True
        assert result.data is not None

    def test_run_returns_result_type(self) -> None:
        instance = FastapiRagKit()
        result = instance.run()
        assert result.error is None
