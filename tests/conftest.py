import pytest

from tests.testlibraries.instance_resource import InstanceResource
from videoarchiver import CONFIG


@pytest.fixture
def yaml_config_load():
    """This fixture prepares YAML config file and loads it."""
    CONFIG.load(InstanceResource.PATH_FILE_CONFIG_FOR_TEST)
    yield
