import os
import pytest
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from richtext.rich_text import rt, RichText


@pytest.mark.parametrize("style,expected_code", [
    ("ok", "\x1b[32mTest\x1b[0m"),
    ("warn", "\x1b[38;5;226mTest\x1b[0m"),
    ("error", "\x1b[31mTest\x1b[0m"),
])
def test_shortcuts(style, expected_code):
    result = getattr(rt, style)("Test")
    assert result == expected_code

@pytest.mark.parametrize("style,expected_code", [
    ('bold', '\x1b[1mTest\x1b[0m'),
    ('faint', '\x1b[2mTest\x1b[0m'),
    ('italic', '\x1b[3mTest\x1b[0m'),
    ('underline', '\x1b[4mTest\x1b[0m'),
    ('blink', '\x1b[5mTest\x1b[0m'),
    ('reverse', '\x1b[7mTest\x1b[0m'),
    ('strikethrough', '\x1b[9mTest\x1b[0m'),
])
def test_styling_shortcuts(style, expected_code):
    styled = getattr(rt, style)
    assert str(styled + 'Test' + rt.reset) == expected_code

@pytest.mark.parametrize("color,expected_code", [
    ('black', '\x1b[30mhello\x1b[0m'),
    ('red', '\x1b[31mhello\x1b[0m'),
    ('green', '\x1b[32mhello\x1b[0m'),
    ('yellow', '\x1b[33mhello\x1b[0m'),
    ('blue', '\x1b[34mhello\x1b[0m'),
    ('magenta', '\x1b[35mhello\x1b[0m'),
    ('cyan', '\x1b[36mhello\x1b[0m'),
    ('white', '\x1b[37mhello\x1b[0m'),
    ('gray', '\x1b[90mhello\x1b[0m'),
    ('grey', '\x1b[90mhello\x1b[0m'),
    ('brightred', '\x1b[91mhello\x1b[0m'),
    ('brightgreen', '\x1b[92mhello\x1b[0m'),
    ('brightyellow', '\x1b[93mhello\x1b[0m'),
    ('brightblue', '\x1b[94mhello\x1b[0m'),
    ('brightmagenta', '\x1b[95mhello\x1b[0m'),
    ('brightcyan', '\x1b[96mhello\x1b[0m'),
    ('brightwhite', '\x1b[97mhello\x1b[0m'),
])
def test_colorize_basic(color, expected_code):
    result = rt.colorize('hello', color)
    assert result == expected_code

def test_style_with_multiple_flags():
    result = rt.style("hi", color="blue", bold=True, underline=True)
    assert result.startswith("\x1b[")
    assert "1" in result  # bold
    assert "4" in result  # underline
    assert "34" in result  # blue
    assert result.endswith("hi\x1b[0m")

def test_rgb_validation_success():
    assert rt.custom_foreground("hi", 120, 200, 255) == "\x1b[38;2;120;200;255mhi\x1b[0m"

def test_rgb_validation_failure():
    with pytest.raises(ValueError):
        rt.custom_foreground("hi", -1, 300, "bad")

def test_hex_color_support():
    result = rt.custom_foreground("hi", r=None, g=None, b=None, hex_color="#ffcc00")
    assert result == "\x1b[38;2;255;204;0mhi\x1b[0m"

def test_mutual_exclusion_rgb_and_hex():
    with pytest.raises(ValueError):
        rt.custom_foreground("hi", r=255, g=204, b=0, hex_color="#ffcc00")

def test_style_repr():
    assert repr(rt).startswith("RichText(styles=")

def test_reset_property():
    assert rt.reset == "\x1b[0m"

def test_RGB_out_of_range():
    with pytest.raises(ValueError):
        rt.custom_foreground('hello', r=2, g=200, b=256)

def test_no_style():
    result = rt.style('hello')
    assert result == "hello"

def test_missing_RGB():
    with pytest.raises(TypeError):
        rt.custom_foreground('hello')

def test_invalid_style():
    with pytest.raises(ValueError):
        rt.colorize('hello', color='Test')


