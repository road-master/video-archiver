from bs4 import BeautifulSoup

from tests.testlibraries.instance_resource import FILE_HTML_PROGRAM_HOME, FILE_HTML_EPISODE, \
    FILE_JSON_EPISODE_DATA_EXAMPLE_01, FILE_JSON_EPISODE_DATA_EXAMPLE_02, FILE_JSON_EPISODE_DATA_EXAMPLE_03, \
    InstanceResource
from videoarchiver.tvasahi.episode_loader import EpisodeLoader
from videoarchiver.tvasahi.html_analyzer import HtmlAnalyzer


class TestEpisodeLoader:
    @staticmethod
    def test_load_backup():
        list_episode = EpisodeLoader(InstanceResource.PATH_TEST_RESOURCES).load_backup('test_tgs')
        assert len(list_episode) == 3
        assert list_episode[0].episode_name == '中野サンプラザ公演振り返り！特別生配信'

    @staticmethod
    def test_list_up_episode(requests_mock, tmp_path):
        program_id_string = 'tgs'
        requests_mock.get(
            f'https://mv.tv-asahi.co.jp/douga/{program_id_string}',
            text=FILE_HTML_PROGRAM_HOME.read_text(encoding='utf-8')
        )
        requests_mock.get(
            'https://mv.tv-asahi.co.jp/douga/api/list/episodes?key=332&limit=12&sort=104&page=1&bought=1',
            text=FILE_JSON_EPISODE_DATA_EXAMPLE_01.read_text(encoding='utf-8')
        )
        requests_mock.get(
            'https://mv.tv-asahi.co.jp/douga/api/list/episodes?key=332&limit=12&sort=104&page=2&bought=1',
            text=FILE_JSON_EPISODE_DATA_EXAMPLE_02.read_text(encoding='utf-8')
        )
        requests_mock.get(
            'https://mv.tv-asahi.co.jp/douga/api/list/episodes?key=332&limit=12&sort=104&page=3&bought=1',
            text=FILE_JSON_EPISODE_DATA_EXAMPLE_03.read_text(encoding='utf-8')
        )
        EpisodeLoader(tmp_path).list_up_episode(program_id_string)

    @staticmethod
    def test__list_up_episode(requests_mock, tmp_path):
        requests_mock.get(
            'https://mv.tv-asahi.co.jp/douga/api/list/episodes?key=332&limit=12&sort=104&page=1&bought=1',
            text=FILE_JSON_EPISODE_DATA_EXAMPLE_01.read_text(encoding='utf-8')
        )
        requests_mock.get(
            'https://mv.tv-asahi.co.jp/douga/api/list/episodes?key=332&limit=12&sort=104&page=2&bought=1',
            text=FILE_JSON_EPISODE_DATA_EXAMPLE_02.read_text(encoding='utf-8')
        )
        requests_mock.get(
            'https://mv.tv-asahi.co.jp/douga/api/list/episodes?key=332&limit=12&sort=104&page=3&bought=1',
            text=FILE_JSON_EPISODE_DATA_EXAMPLE_03.read_text(encoding='utf-8')
        )
        html_analyzer = HtmlAnalyzer(BeautifulSoup(FILE_HTML_EPISODE.read_text(encoding='utf-8'), "html.parser"))
        program_id_string = 'tgs'
        with (tmp_path / f'{program_id_string}.yml').open(
                'w', encoding='UTF-8', newline='\n'
        ) as file_backup:
            # pylint: disable=protected-access
            list_episode = EpisodeLoader._list_up_episode(file_backup, html_analyzer, program_id_string)
        assert list_episode[0].episode_name == '中野サンプラザ公演振り返り！特別生配信'
