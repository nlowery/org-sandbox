from utilities.themes import Theme
import unittest

class ThemeTests(unittest.TestCase):

    def setUp(self):
        self.theme = Theme(theme='default')

    def test_theme_init(self):
        self.assertEqual(self.theme.background_animated, False)
        self.assertEqual(self.theme.organism_scale, 1)
        self.assertEqual(self.theme.food_scale, 1)
