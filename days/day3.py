import string

from typing import List


LOWER_PRIORITY_MAP = dict(zip(string.ascii_lowercase, range(1, 27)))
HIGHER_PRIORITY_MAP = dict(zip(string.ascii_uppercase, range(27, 53)))


def get_matching_ordinance(rucksack: List[str], use_thirds=False) -> str:
    if use_thirds:
        priority = set(list(rucksack[0])) & set(list(rucksack[1])) & set(list(rucksack[2]))
    else:
        rucksack = rucksack[0]
        sep = len(rucksack) // 2
        compartment_a = rucksack[:sep]
        compartment_b = rucksack[sep:]
        priority = set(list(compartment_a)) & set(list(compartment_b))

    if len(priority) == 0:
        return ""
    return priority.pop()


def get_priority_total_from_rucksack(data: List[str], use_thirds: bool = False):
    priority_total = 0

    if use_thirds:
        start_index = 0
        current_index = 3
        while current_index <= len(data):
            priority = get_matching_ordinance(data[start_index: current_index], use_thirds)
            points = LOWER_PRIORITY_MAP.get(priority) or HIGHER_PRIORITY_MAP.get(priority) or 0
            priority_total += points

            # shift starting and current index forward
            start_index = current_index
            current_index += 3
    else:
        for rucksack in data:
            priority = get_matching_ordinance([rucksack])
            points = LOWER_PRIORITY_MAP.get(priority) or HIGHER_PRIORITY_MAP.get(priority) or 0
            priority_total += points

    return priority_total


def run(part: str, data: List[str]):
    if part == 'a':
        return get_priority_total_from_rucksack(data)

    if part == 'b':
        return get_priority_total_from_rucksack(data, True)
