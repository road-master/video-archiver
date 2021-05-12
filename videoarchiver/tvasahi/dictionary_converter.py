from typing import Dict, List, Optional, Union

from videoarchiver.tvasahi.models import Episode


class DictionaryConverter:
    @classmethod
    def convert_to_list(cls, list_dictionary_episode: List[dict]) -> List[Episode]:
        return [cls.convert_to_model(dictionary_episode) for dictionary_episode in list_dictionary_episode]

    @staticmethod
    def convert_to_model(dict_episode: Dict[str, Optional[Union[int, str]]]) -> Episode:
        dict_episode_lower_case = {k.lower(): v for k, v in dict_episode.items()}
        # noinspection PyTypeChecker
        return Episode.schema(unknown="EXCLUDE").load(dict_episode_lower_case)  # type: ignore
