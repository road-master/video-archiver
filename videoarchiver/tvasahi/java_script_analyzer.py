class JavaScriptAnalyzer:
    def __init__(self, java_script: str):
        self.lines_java_script = java_script.splitlines()

    def extract_variable(self, variable_name: str):
        return self.extract_variable_from_definition_line(self.__find_first_line(f'var {variable_name}'))

    def extract_url_playlist(self):
        return self.extract_url_from_definition_line(self.__find_first_line('m3u8'))

    def __find_first_line(self, key_word: str):
        for line_java_script in self.lines_java_script:
            if key_word in line_java_script:
                return line_java_script
        raise ValueError(f"Variable isn't included. key_word = '{key_word}'")

    @staticmethod
    def extract_variable_from_definition_line(definition_line: str):
        """Warning: string value is not supported !"""
        return int(definition_line.rsplit('=', 2)[1].strip().strip(';'))

    @staticmethod
    def extract_url_from_definition_line(definition_line: str):
        for part in definition_line.rsplit('"'):
            if part.startswith('https://www2.uliza.jp'):
                return part
        raise ValueError(f"URL to uliza isn't included. definition_line = '{definition_line}'")
