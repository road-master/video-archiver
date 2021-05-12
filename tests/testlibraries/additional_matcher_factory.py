import urllib.parse
from typing import Callable, Dict

from requests import PreparedRequest


class AdditionalMatcherFactory:
    """@see https://requests-mock.readthedocs.io/en/latest/matching.html#additional-matchers"""

    @staticmethod
    def create_request_data_matcher(data: Dict[str, str]) -> Callable[[PreparedRequest], bool]:
        def additional_matcher(request: PreparedRequest):
            return request.body == "&".join(
                [f"{urllib.parse.quote(key)}={urllib.parse.quote(value)}" for key, value in data.items()]
            )

        return additional_matcher
