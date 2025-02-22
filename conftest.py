import pytest


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": ["authorization", "api-key", "host"],
        "filter_query_parameters": ["key"],
    }

def rewrite_response_header(key, new_value=''):
    def before_record_response(response):
        response['headers'][key] = new_value
        return response
    return before_record_response


def pytest_recording_configure(config, vcr):
    vcr.serializer = "yaml"
    vcr.decode_compressed_response = True
    vcr.before_record_response = rewrite_response_header('Set-Cookie', 'cookie')
