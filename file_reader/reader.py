import pathlib
from typing import List

BASE_DIR = pathlib.PurePath(__file__).parent.parent
INPUT_DIR = f"{BASE_DIR}/input"


class InputReader(object):
    def __init__(self, data: List[str]):
        self.data = data

    @classmethod
    def read_day_input(cls, day: str, part: str):
        file_name = f"{INPUT_DIR}/{day}_{part}.txt"
        with open(file_name) as f:
            data = [line.rstrip("\n") for line in f.readlines()]
        return cls(data)
