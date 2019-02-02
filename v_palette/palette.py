"""
    This library provides an easy way to call Material Colors from python.

    Available colors: https://material.io/guidelines/style/color.html#color-color-palette
"""

from .colors import MATERIAL


_VALID_COLORS = list(MATERIAL.keys())
_VALID_INDEXS = [50] + [100*x for x in range(1, 10)]


def get_one_color(name, index):
    """
        Gives one color based on it's name and index.

        Available colors: https://material.io/guidelines/style/color.html#color-color-palette

        Args:
            name:   name of the color
            index:  intesity of the color
    """
    if name.lower() not in _VALID_COLORS:
        raise ValueError(f"Color '{name}' is not valid. Valid colors are: {_VALID_COLORS}")

    if index not in _VALID_INDEXS:
        raise ValueError(f"Index {index} is not valid. Valid indexs are {_VALID_INDEXS}")

    return MATERIAL[name.lower()][index]


def get_colors(data):
    """
        Gives hex colors.

        You can pass a tuple with name and index. Example:
            get_colors(("red", 100)) --> "#FFCDD2"

        Or a list of tuples with name and index. Examples:
            get_colors([("red", 100)]) --> ["#FFCDD2"]
            get_colors([("red", 100), ("blue", 100)]) --> ["#FFCDD2", "#BBDEFB"]

        Available colors: https://material.io/guidelines/style/color.html#color-color-palette

        Args:
            data:   tuple with (name, index) or a list of this tuples

        Returns:
            if input was a list --> list of hex colors
            if input was a tuple --> hex color
    """

    # If it is a list, return a list of colors
    if isinstance(data, list):
        return [get_one_color(name, index) for name, index in data]

    # If it is a tuple, return one color
    return get_one_color(data[0], data[1])
