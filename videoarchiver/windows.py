class Windows:
    DICTIONARY_DISALLOW_CHARACTER = {
        '<': '＜',
        '>': '＞',
        ':': '：',
        '"': '”',
        '/': '／',
        '\\': '＼',
        '|': '｜',
        '?': '？',
        '*': '＊',
    }
    @staticmethod
    def replace_disallow_character(string):
        return string.translate(str.maketrans(Windows.DICTIONARY_DISALLOW_CHARACTER))
