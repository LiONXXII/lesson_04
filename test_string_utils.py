import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# ==================== 1. ТЕСТЫ ДЛЯ capitalize ====================

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# ==================== 2. ТЕСТЫ ДЛЯ trim ======================

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello world", "hello world"),
    ("   python", "python"),
    ("  text  ", "text  "),  # пробелы между слов и в конце остаются
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", ""),
    ("   ", ""),
    (None, None),
    ("123abc", "123abc"),  # без пробелов ничего не меняется
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# ==================== 3. ТЕСТЫ ДЛЯ contains ====================

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "U", False),
    ("hello", "o", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "S", False),
    (" ", "a", False),
    ("abc", "", False),  # пустой символ
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


# ==================== 4. ТЕСТЫ ДЛЯ delete_symbol ====================

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello", "l", "heo"),
    ("python", "p", "ython"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "a", ""),
    ("abc", "d", "abc"),  # символа нет - ничего не удаляется
    ("abc", "", "abc"),   # пустой символ
    (None, "a", None),
    (" ", " ", ""),       # пробел как символ - удаляется
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
