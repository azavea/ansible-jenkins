import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):

    """ Load default variables into dictionary.

    Args:
        Ansible - Requires the ansible connection backend.
    """
    return Ansible("include_vars", "./defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleFacts(Ansible):

    """ Load ansible facts into a dictionary.

    Args:
        Ansible - Requires ansible connection backend.
    """
    return Ansible("setup")["ansible_facts"]


def test_jenkins_package(Package, AnsibleDefaults):

    """ Ensure jenkins package is both installed and at the proper major
    version.

    Args:
        Package - module to determine package install status and version.
        AnsibleDefaults - module to pull the target version of Jenkins.

    Raises:
        AssertionError if package is not installed or the wrong version.
    """
    jenkins = Package("jenkins")
    assert jenkins.is_installed
    jenkins_major_version = AnsibleDefaults["jenkins_major_version"]
    assert jenkins.version.startswith(jenkins_major_version)


def test_jenkins_service(Service, Sudo):

    """ Ensure Jenkins service is enabled and running.

    Args:
        Service: module used to determine jenkins service status.
        Sudo: module used for privilege elevation.

    Raises:
        AssertionError if service isn't enabled and running.
    """

    jenkins = Service("jenkins")
    with Sudo():
        assert jenkins.is_enabled
        assert jenkins.is_running


def test_jenkins_connection(Socket, Sudo, AnsibleDefaults):

    """ Ensure that jenkins is listening on the proper port.

    Args:
        Socket: module used to get OS socket information.
        Sudo: module used for privilege elevation.
        AnsibleDefaults: module to pull the jenkins_http_port.

    Raises:
        AssertionError if the proper port is not listening.
    """
    jenkins_port = AnsibleDefaults["jenkins_http_port"]
    jenkins_socket = Socket("tcp://0.0.0.0:{}".format(jenkins_port))
    with Sudo():
        assert jenkins_socket.is_listening
