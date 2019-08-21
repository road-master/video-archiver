from pathlib import Path
from typing import List, TextIO

import yaml

from videoarchiver.tvasahi.dictionary_converter import DictionaryConverter
from videoarchiver.tvasahi.html_analyzer import HtmlAnalyzer
from videoarchiver.tvasahi.models import Episode
from videoarchiver.tvasahi.client_for_back_end import ClientForBackEnd, Payload


class EpisodeLoader:
    def __init__(self, path_directory_cache: Path):
        self.path_directory_cache = path_directory_cache

    def load_backup(self, program_id_string: str) -> List[Episode]:
        with (self.path_directory_cache / f'{program_id_string}.yml').open(
                'r', encoding='UTF-8', newline='\n'
        ) as file_backup:
            list_dictionary_episode = yaml.safe_load(file_backup)
            return DictionaryConverter.convert_to_list(list_dictionary_episode)

    def list_up_episode(self, program_id_string: str) -> List[Episode]:
        html_analyzer = HtmlAnalyzer(ClientForBackEnd.request_program_home_page(program_id_string))
        with (self.path_directory_cache / f'{program_id_string}.yml').open(
                'w', encoding='UTF-8', newline='\n'
        ) as file_backup:
            # ↓ @see https://github.com/python/mypy/issues/2337
            # ↓ @see https://github.com/python/mypy/pull/3299
            return self._list_up_episode(file_backup, html_analyzer, program_id_string)  # type: ignore

    @classmethod
    def _list_up_episode(
            cls, file_backup: TextIO, html_analyzer: HtmlAnalyzer, program_id_string: str
    ) -> List[Episode]:
        program_code = html_analyzer.extract_episode_code()
        sort = html_analyzer.extract_sort()
        max_page = None
        current_page = 1
        list_episode = []
        while max_page is None or max_page >= current_page:
            dictionary_json = ClientForBackEnd.request_api_list_episode(
                program_id_string, Payload(program_code, 12, sort, current_page)
            )
            list_dictionary_episode = dictionary_json['data']
            file_backup.write(yaml.dump(list_dictionary_episode, allow_unicode=True, default_flow_style=False))
            list_episode.extend(
                DictionaryConverter.convert_to_list(list_dictionary_episode)
            )
            max_page = dictionary_json['info']['max_page']
            current_page += 1
        return list_episode
