from typing import List


def get_highest_calorie_count(current_count, current_highest):
    return max(current_count, current_highest)


def a(data: List[str]) -> int:
    highest_calorie_count = 0
    current_calorie_count = 0

    for calorie in data:
        if not calorie:
            highest_calorie_count = get_highest_calorie_count(current_calorie_count, highest_calorie_count)
            current_calorie_count = 0
            continue
        current_calorie_count += int(calorie)

    # clear out any remaining calorie count
    return get_highest_calorie_count(current_calorie_count, highest_calorie_count)


def run(part: str, data: List[str]):
    if part == 'a':
        return a(data)

    if part == 'b':
        raise NotImplementedError("part b is not ")
