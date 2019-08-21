from requests.cookies import create_cookie

from tests.testlibraries.additional_matcher_factory import AdditionalMatcherFactory
from tests.testlibraries.cookie_jar_factory import RequestsCookieJarFactory
from videoarchiver.niconico.client_for_back_end import ClientForBackEnd
COOKIES_LOGIN_EXAMPLE = RequestsCookieJarFactory.create([
    create_cookie(
        'nicosid',
        '1564771509.1274701801',
        domain='.nicovideo.jp',
        path='/',
        expires=1880131509,
        discard=False,
        rest={},
    ),
    create_cookie(
        'registrationActionTrackId',
        'rwVWhn4GAx_1564771509996',
        domain='.nicovideo.jp',
        path='/',
        secure=True,
        expires=1564814709,
        discard=False,
    ),
])


class TestClientForBackEnd:
    # pylint: disable=unused-argument
    @staticmethod
    def test_login(requests_mock, yaml_config_load):
        print()
        mail_address = 'mail@address.niconico'
        password = 'password_niconico'
        requests_mock.post(
            'https://account.nicovideo.jp/api/v1/login',
            # allow_redirects=False,
            cookies=COOKIES_LOGIN_EXAMPLE,
            additional_matcher=AdditionalMatcherFactory.create_request_data_matcher(
                {'LOGIN_ID': mail_address, 'PASSWORD': password}
            )
        )
        assert ClientForBackEnd.login() == COOKIES_LOGIN_EXAMPLE
