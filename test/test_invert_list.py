import unittest

from src.invert_list import invert_list


class TestUtils(unittest.TestCase):

    def test_invert_empty_list(self):

        self.assertEqual([], invert_list([]))