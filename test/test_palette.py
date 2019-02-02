"""
    Tests for v_palette.py
"""

import unittest

from v_palette.palette import get_colors


class TestUtilities(unittest.TestCase):
    """Test utilities"""

    # ------------------------------ palette -------------------------------------------------------
    def test_palette(self):
        """
            Test palette
        """

        # Test that you can call one color with a list of tuples or with a tuple
        self.assertEqual(get_colors([("red", 100)]), "#FFCDD2")
        self.assertEqual(get_colors(("red", 100)), "#FFCDD2")

        # Test that you can call more than one color
        self.assertEqual(
            get_colors([("red", 100), ("blue", 100)]),
            ["#FFCDD2", "#BBDEFB"]
        )
