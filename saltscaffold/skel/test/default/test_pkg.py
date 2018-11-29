
import pytest
import os

@pytest.mark.parametrize("pkgname", [
    "${formula_name}",
])

def test_pkg(host, pkgname):
    pkg = host.package(pkgname)
    assert pkg.is_installed is True
