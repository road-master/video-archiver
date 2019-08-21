from videoarchiver.windows import Windows


class TestWindows:
    @staticmethod
    def test_replace_disallow_character():
        assert Windows.replace_disallow_character(r'test<>:"/\|?*') == 'test＜＞：”／＼｜？＊'
