import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('li', 'yuan')
        self.assertEqual(formatted_name, 'Li Yuan')


unittest.main
