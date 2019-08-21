from tests.testlibraries.instance_resource import COOKIES_STREAMING_EXAMPLE
from videoarchiver.cookie_converter import CookieConverter


class TestCookieConverter:
    @staticmethod
    def test_convert_cookie_dict_to_string():
        assert CookieConverter.convert_requests_cookie_jar_to_string(COOKIES_STREAMING_EXAMPLE) == (
            'uliza_iphone_auth_11495462=z8uoLuqz+G97gH91i0iFe01ognvP1KZX11H0krLY+0c=?'
            'guid=15a03256-2346-4c46-b308-3221376d20b2&'
            'allowurl=https://www2.uliza.jp/&'
            'v=11495464:1561090903,11495462:1561090903,11495463:1561090903&'
            '_expire=1561108903;'
            'uliza_iphone_auth_11495463=z8uoLuqz+G97gH91i0iFe01ognvP1KZX11H0krLY+0c=?'
            'guid=15a03256-2346-4c46-b308-3221376d20b2&'
            'allowurl=https://www2.uliza.jp/&'
            'v=11495464:1561090903,11495462:1561090903,11495463:1561090903&'
            '_expire=1561108903;'
            'uliza_iphone_auth_11495464=z8uoLuqz+G97gH91i0iFe01ognvP1KZX11H0krLY+0c=?'
            'guid=15a03256-2346-4c46-b308-3221376d20b2&'
            'allowurl=https://www2.uliza.jp/&'
            'v=11495464:1561090903,11495462:1561090903,11495463:1561090903&'
            '_expire=1561108903'
        )
