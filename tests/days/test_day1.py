from unittest import TestCase

from days.day1 import get_ordered_calorie_count, run


class TestDay1(TestCase):
    def setUp(self):
        self.data = ["1", "22", "", "10", "4", "", "55", "", "100", "", "7", ""]

    def test_get_ordered_calorie_count(self):
        results = get_ordered_calorie_count(self.data)
        self.assertTrue(len(results), 5)
        self.assertTrue(results[0], 100)
        self.assertTrue(results[-1], 7)

    def test_run_part_a(self):
        results = run("a", self.data)
        self.assertTrue(results, 100)

    def test_run_part_b(self):
        results = run("b", self.data)
        self.assertTrue(results, 178)
