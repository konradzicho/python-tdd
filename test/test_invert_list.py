import unittest

from src.invert_list import invert_list


class TestUtils(unittest.TestCase):

    def test_invert_empty_list(self):
        self.assertEqual([], invert_list([]))

    def test_invert_list_with_two_elements(self):
        self.assertEqual([2,1], invert_list([1,2]))

    def test_invert_list_with_1_4(self):
        self.assertEqual([4,1], invert_list([1,4]))

    def test_invert_list_with_3_1(self):
        self.assertEqual([1,3], invert_list([3,1]))

    def test_invert_list_with_one_element(self):
        self.assertEqual([1], invert_list([1]))

    def test_invert_list_with_three_elements(self):
        ll = [1, 2, 3]
        self.assertEqual([3,2,1], invert_list(ll))
        self.assertEqual(ll, [1,2,3])

#    def test_invert_none_argument(self):
#        self.assertEqual([], invert_list([]))
#       self.assertRaises(ValueError("no argument"), invert_list(None))

