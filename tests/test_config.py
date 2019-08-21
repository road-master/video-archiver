from tests.testlibraries.instance_resource import InstanceResource
from videoarchiver import Config


class TestConfig:
    @staticmethod
    def test_load():
        config = Config()
        config.load(InstanceResource.PATH_FILE_CONFIG_FOR_TEST)
        config_tb_asahi = config.tv_asahi
        assert config_tb_asahi.mail_address == 'mail@address.tv.asahi'
        assert config_tb_asahi.password == 'password_tv_asahi'
        # pylint: disable=unsubscriptable-object
        assert config_tb_asahi.list_program_id[0] == 'tgs'
        assert config_tb_asahi.list_program_id[1] == 'joshiryu_logirl'
        config_niconico = config.niconico
        assert config_niconico.mail_address == 'mail@address.niconico'
        assert config_niconico.password == 'password_niconico'
        assert config_niconico.list_program_id[0] == 'lv61315784'
        assert config_niconico.list_program_id[1] == 'lv83183479'
