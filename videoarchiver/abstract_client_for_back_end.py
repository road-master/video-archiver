from abc import ABC, abstractmethod

from requests.cookies import RequestsCookieJar


class AbstractClientForBackEnd(ABC):
    @classmethod
    @abstractmethod
    def login(cls) -> RequestsCookieJar:
        raise NotImplementedError()
