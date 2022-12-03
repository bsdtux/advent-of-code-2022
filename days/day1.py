from typing import List


def get_ordered_calorie_count(data: List[str]) -> List[int]:
    calorie_counts = []
    current_calorie_count = 0

    for calorie in data:
        if not calorie:
            calorie_counts.append(current_calorie_count)
            current_calorie_count = 0
            continue
        current_calorie_count += int(calorie)

    # clear out any remaining calorie count
    if current_calorie_count > 0:
        calorie_counts.append(current_calorie_count)
    calorie_counts.sort(reverse=True)
    return calorie_counts


def run(part: str, data: List[str]):
    calorie_counts = get_ordered_calorie_count(data)
    if part == "a":
        return calorie_counts[0]

    if part == "b":
        return sum(calorie_counts[:3])
