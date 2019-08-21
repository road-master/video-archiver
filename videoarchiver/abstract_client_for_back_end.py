from abc import abstractmethod, ABC

from requests.cookies import RequestsCookieJar


class AbstractClientForBackEnd(ABC):
    @classmethod
    @abstractmethod
    def login(cls) -> RequestsCookieJar:
        raise NotImplementedError()
