### VCR record/replay LLM testing

This is a simple example of how to use VCR to record and replay LLM tests.

[pytest-recording](https://github.com/kiwicom/pytest-recording) is a pytest plugin that allows you to record and replay HTTP interactions in your tests. It is based on [VCR.py](https://github.com/kevin1024/vcrpy)

### Run all tests

`uv run pytest tests/`

## Rewrite recorded cassettes with new LLM responses

`uv run pytest tests/ --vcr-record=rewrite`


## Important configuration

- `conftest.py` contains the VCR configuration to exclude authentication headers from the recorded cassettes, decompress gzipped output response. NOTE: Different LLMs pass the key differently. For example. `Authorization` header is used by some LLMs, while others a request parameter. You may need to adjust the configuration accordingly.
- `tests/cassettes/test_run` contains the recorded cassette
- `tests/test_run.py` contains the tests that use the recorded cassette
- `.pre-commit-config.yaml` contains the pre-commit configuration to ensure any secrets are not checked-in.