import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from colors import COLORS


class TestColorConstants(unittest.TestCase):
    # Verify that colors are following the RGB format (X, Y, Z) where the numbers are 0 ... 255
    def test_color_format(self):
        for color_name, color_value in COLORS.items():
            with self.subTest(color=color_name):
                self.assertIsInstance(color_value, tuple)
                self.assertEqual(len(color_value), 3)
                for value in color_value:
                    self.assertIsInstance(value, int)
                    self.assertGreaterEqual(value, 0)
                    self.assertLessEqual(value, 255)


if __name__ == "__main__":
    unittest.main()
