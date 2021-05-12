from requests.cookies import RequestsCookieJar


class CookieConverter:
    @staticmethod
    def convert_requests_cookie_jar_to_string(requests_cookie_jar: RequestsCookieJar) -> str:
        cookie_dict = requests_cookie_jar.get_dict()
        return ";".join([f"{key}={value}" for key, value in cookie_dict.items()])
