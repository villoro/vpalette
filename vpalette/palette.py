"""
    This library provides an easy way to call colors from palettes using python.

    Available colors:
        - Vtint: https://www.tints.dev/?red=FF5722&pink=EC4899&fuchsia=D946EF&purple=A855F7&amethyst=9B59B6&indigo=6366F1&blue=3B82F6&sky=0EA5E9&cyan=06B6D4&teal=14B8A6&emerald=10B981&green=22C55E&olive=8BC34A&lime=CDDC39&yellow=FFEB3B&amber=FFC107&orange=FF9800&brown=795548&stone=78716C&asphalt=34495E&grey=9E9E9E
        - Material: https://material.io/guidelines/style/color.html#color-color-palette
        - Flat: https://htmlcolorcodes.com/color-chart/flat-design-color-chart/
        - Tailwind: https://uicolors.app/browse/tailwind-colors
"""

from .colors import COLORS


_VALID_INDEXS = [50] + [100 * x for x in range(1, 10)]


def get_valid_colors():
    """Gives a list of valid colors"""

    valid_colors = []
    for data in COLORS.values():
        valid_colors += list(data.keys())

    return list(set(valid_colors))


def get_one_color(name, index, palette="vtint"):
    """
    Gives one color based on it's name and index.

    Available colors:
    - [default] Vtint: https://www.tints.dev/?red=FF5722&pink=EC4899&fuchsia=D946EF&purple=A855F7&amethyst=9B59B6&indigo=6366F1&blue=3B82F6&sky=0EA5E9&cyan=06B6D4&teal=14B8A6&emerald=10B981&green=22C55E&olive=8BC34A&lime=CDDC39&yellow=FFEB3B&amber=FFC107&orange=FF9800&brown=795548&stone=78716C&asphalt=34495E&grey=9E9E9E
    - Material: https://material.io/guidelines/style/color.html#color-color-palette
    - Flat: https://htmlcolorcodes.com/color-chart/flat-design-color-chart/
    - Tailwind: https://uicolors.app/browse/tailwind-colors

    If the color is not found it will look at the other palettes.

    Args:
        name:       name of the color
        index:      intesity of the color
        palette:    name of the palette with colors ['material', 'flat']
    """

    name = name.lower()
    palette = palette.lower()

    # Check index
    if index not in _VALID_INDEXS:
        raise ValueError(f"Index {index} is not valid. Valid indexs are {_VALID_INDEXS}")

    # Try to return it from the asked palette
    if name in COLORS[palette]:
        return COLORS[palette][name][index]

    # Check if it is possible to retrive the color from other palettes
    for other_palette, data in COLORS.items():
        if name in COLORS[other_palette]:
            return COLORS[other_palette][name][index]

    # If color not found raise error
    raise ValueError(f"Color '{name}' is not valid. Valid colors are: {get_valid_colors()}")


def get_colors(data, palette="vtint"):
    """
    Gives hex colors.

    You can pass a tuple with name and index. Example:
        get_colors(("red", 100)) --> "#FFCDD2"

    Or a list of tuples with name and index. Examples:
        get_colors([("red", 100)]) --> ["#FFCDD2"]
        get_colors([("red", 100), ("blue", 100)]) --> ["#FFCDD2", "#BBDEFB"]

    Available colors:
    - [default] Vtint: https://www.tints.dev/?red=FF5722&pink=EC4899&fuchsia=D946EF&purple=A855F7&amethyst=9B59B6&indigo=6366F1&blue=3B82F6&sky=0EA5E9&cyan=06B6D4&teal=14B8A6&emerald=10B981&green=22C55E&olive=8BC34A&lime=CDDC39&yellow=FFEB3B&amber=FFC107&orange=FF9800&brown=795548&stone=78716C&asphalt=34495E&grey=9E9E9E
    - Material: https://material.io/guidelines/style/color.html#color-color-palette
    - Flat: https://htmlcolorcodes.com/color-chart/flat-design-color-chart/
    - Tailwind: https://uicolors.app/browse/tailwind-colors

    Args:
        data:       tuple with (name, index) or a list of this tuples
        palette:    name of the palette with colors ['material', 'flat']

    Returns:
        if input was a list --> list of hex colors
        if input was a tuple --> hex color
    """

    # If it is a list, return a list of colors
    if isinstance(data, list):
        return [get_one_color(name, index, palette) for name, index in data]

    # If it is a tuple, return one color
    return get_one_color(data[0], data[1], palette)
