
import pytest
import os

@pytest.mark.parametrize("servicename", [
    "${formula_name}",
])

def test_service(host,servicename):
    service = host.service(servicename)
    assert service.is_enabled
    assert service.is_running
