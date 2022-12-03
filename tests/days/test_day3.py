from unittest import TestCase
from days.day3 import get_matching_ordinance, get_priority_total_from_rucksack


class TestDay3(TestCase):
    def setUp(self):
        self.data = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]

    def test_get_matching_ordinance(self):
        expected = "p"
        self.assertEqual(get_matching_ordinance([self.data[0]]), expected)

    def test_get_matching_ordinance(self):
        expected = "r"
        self.assertEqual(get_matching_ordinance(self.data[:3], True), expected)

    def test_get_matching_priority_total(self):
        expected = 157
        self.assertEqual(get_priority_total_from_rucksack(self.data), expected)

    def test_get_matching_priority_three_total(self):
        expected = 70
        self.assertEqual(get_priority_total_from_rucksack(self.data, True), expected)
