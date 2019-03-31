"""
    Tests for v_palette.py
"""

import unittest

from v_palette.palette import get_colors, get_one_color


class TestPalette(unittest.TestCase):
    """Test palette"""

    def test_from_tuple(self):
        """ Test that you can pass a tuple to get one color """

        self.assertEqual(get_colors(("red", 100)), "#FFCDD2")

    def test_from_list_of_tuples(self):
        """ Test that you can pass a list of tuples to get a list of colors """

        self.assertEqual(get_colors([("red", 100)]), ["#FFCDD2"])

        # Same but with two colors
        self.assertEqual(get_colors([("red", 100), ("blue", 100)]), ["#FFCDD2", "#BBDEFB"])

    def test_invalid_params(self):
        """ Test that raises ValueError when input params are wrong """

        # Wrong color name
        self.assertRaises(ValueError, get_one_color, "imaginary", 100)

        # Wrong color index
        self.assertRaises(ValueError, get_one_color, "red", 77)

    def test_both_palettes(self):
        """ Test that handles well other palettes """

        # Request a color from default palette
        self.assertEqual(get_colors(("orange", 100)), "#FFE0B2")

        # Request from other palettes
        self.assertEqual(get_colors(("silver", 100)), "#F2F3F4")
        self.assertEqual(get_colors(("orange", 100), palette="flat"), "#FDEBD0")
