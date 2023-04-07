import pytest

from vpalette import __version__
from vpalette.palette import get_colors, get_one_color


def test_version():
    assert __version__ == "2.0.1"


def test_from_tuple():
    """Test that you can pass a tuple to get one color"""

    assert get_colors(("red", 500)) == "#FF5722"


def test_from_list_of_tuples():
    """Test that you can pass a list of tuples to get a list of colors"""

    assert get_colors([("red", 500)]) == ["#FF5722"]

    # Same but with two colors
    assert get_colors([("red", 500), ("blue", 500)]) == ["#FF5722", "#3B82F6"]


def test_invalid_params():
    """Test that raises ValueError when input params are wrong"""

    # Wrong color name
    with pytest.raises(ValueError):
        get_one_color("imaginary", 100)

    # Wrong color index
    with pytest.raises(ValueError):
        get_one_color("red", 77)


def test_both_palettes():
    """Test that handles well other palettes"""

    # Request a color from default palette
    assert get_colors(("orange", 500)) == "#FF9800"

    # Request from other palettes
    assert get_colors(("silver", 500)) == "#BDC3C7"
    assert get_colors(("orange", 500), palette="flat") == "#F39C12"
