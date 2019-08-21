import json

from tests.testlibraries.instance_resource import FILE_JSON_EPISODE_DATA_EXAMPLE_01
from videoarchiver.tvasahi.dictionary_converter import DictionaryConverter


class TestDictionaryConverter:
    @staticmethod
    def test_convert_to_list():
        """JSON should convert into model."""
        list_episode = DictionaryConverter.convert_to_list(
            json.loads(FILE_JSON_EPISODE_DATA_EXAMPLE_01.read_text(encoding='utf-8'))['data']
        )
        assert list_episode[0].episode_name == '中野サンプラザ公演振り返り！特別生配信'

    @staticmethod
    def test_convert_to_model():
        """JSON should convert into model."""
        episode = DictionaryConverter.convert_to_model(
            json.loads(FILE_JSON_EPISODE_DATA_EXAMPLE_01.read_text(encoding='utf-8'))['data'][0]
        )
        assert episode.episode_name == '中野サンプラザ公演振り返り！特別生配信'
