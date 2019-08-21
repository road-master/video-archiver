from http.cookiejar import Cookie
from typing import List

from requests.cookies import RequestsCookieJar


class RequestsCookieJarFactory:
    @staticmethod
    def create(list_cookie: List[Cookie]) -> RequestsCookieJar:
        cookie_jar = RequestsCookieJar()
        for cookie in list_cookie:
            cookie_jar.set(cookie.name, cookie.value, domain=cookie.domain, path=cookie.path)
        return cookie_jar
