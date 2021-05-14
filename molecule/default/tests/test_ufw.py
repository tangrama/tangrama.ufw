import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package_installed(host):
    pkg = host.package("ufw")

    assert pkg.is_installed


def test_service_enabled(host):
    service = host.service("ufw")

    assert service.is_enabled


def test_service_running(host):
    with host.sudo():
        service = host.service("ufw")
        assert service.is_running


def test_configuration_file_created(host):
    f = host.file('/etc/ufw/user.rules')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize(
    "port, action", [
        ("80", "ACCEPT"),
        ("443", "ACCEPT"),
        ("9322", "ACCEPT"),
    ]
)
def test_configuration_rules(host, port, action):
    with host.sudo():
        f = host.file('/etc/ufw/user.rules')
        rule = f"-A ufw-user-input -p tcp --dport {port} -j {action}"
        assert f.contains(rule)
