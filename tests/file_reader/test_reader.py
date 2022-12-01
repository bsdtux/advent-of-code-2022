import unittest
from file_reader.reader import InputReader


class TestInputReader(unittest.TestCase):
    def test_read_test_file(self):
        test_data = InputReader.read_day_input('test', 'a')
        self.assertTrue(len(test_data.data  ), 7)
