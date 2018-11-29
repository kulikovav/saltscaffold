
import pytest
import os

@pytest.mark.parametrize("confpath", [
    "/etc/config.conf",
])

def test_conf(host,confpath):
    config = host.file(confpath)
    assert config.user == "root"
    assert config.group == "root"
    assert config.mode == 0o444
