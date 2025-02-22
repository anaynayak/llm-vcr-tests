import pytest
from run import generate_response

@pytest.mark.vcr()
def test_generate_response():
    response = generate_response("What is pytest?")
    assert "testing framework" in response.lower()