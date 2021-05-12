import pytest

from tests.testlibraries.instance_resource import FILE_JAVA_SCRIPT_TEST_DATA
from videoarchiver.tvasahi.java_script_analyzer import JavaScriptAnalyzer


class TestJavaScriptAnalyzer:
    @staticmethod
    def test_extract_variable():
        java_script_analyzer = JavaScriptAnalyzer(FILE_JAVA_SCRIPT_TEST_DATA.read_text(encoding="utf-8"))
        assert java_script_analyzer.extract_variable("pg") == 332
        assert java_script_analyzer.extract_variable("sort") == 104

    @staticmethod
    @pytest.mark.parametrize("definition_line, expected", [("  var pg = 332;\n", 332), ("  var sort = 104;\n", 104)])
    def test_extract_variable_from_definition_line(definition_line, expected):
        """Variable should extract from definition line."""
        assert JavaScriptAnalyzer.extract_variable_from_definition_line(definition_line) == expected
