from bs4 import BeautifulSoup

from videoarchiver.tvasahi.java_script_analyzer import JavaScriptAnalyzer


class HtmlAnalyzer:
    def __init__(self, soup: BeautifulSoup):
        self.java_script_analyzer = JavaScriptAnalyzer(
            soup.find("section", id="primary").find("script", type="text/javascript").string
        )

    def extract_episode_code(self):
        return self.java_script_analyzer.extract_variable("pg")

    def extract_sort(self):
        return self.java_script_analyzer.extract_variable("sort")

    @staticmethod
    def extract_url_playlist(soup):
        for script in soup.find_all("script", type="text/javascript"):
            if script.string:
                java_script_analyzer = JavaScriptAnalyzer(script.string)
                try:
                    return java_script_analyzer.extract_url_playlist()
                except ValueError:
                    continue
        raise ValueError("Can't find URL for play list.")
