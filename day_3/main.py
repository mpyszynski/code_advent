from dataclasses import dataclass
from typing import List
from string import ascii_lowercase, ascii_uppercase


@dataclass
class Rucksack:
    inventory: str
    first_compartment: str = ""
    second_compartment: str = ""

    def __init__(self, inv: str):
        self.inventory = inv
        half_length = int(len(inv) / 2)
        self.first_compartment = inv[:half_length]
        self.second_compartment = inv[half_length:]

    def find_duplicated_item(self) -> str:
        for item in self.first_compartment:
            if item in self.second_compartment:
                return item

    def find_duplicated_item_priority(self) -> int:
        item = self.find_duplicated_item()
        return get_item_priority(item)

    def is_item_in_inventory(self, item: str) -> bool:
        if item in self.inventory:
            return True
        return False


def get_item_priority(item: str) -> int:
    alphabet = ascii_lowercase + ascii_uppercase
    for i, letter in enumerate(alphabet):
        if item == letter:
            return i + 1
    return 0


def get_input_data(source: str) -> List[str]:
    f = open(source, "r")
    content = f.readlines()
    f.close()
    return [c.strip() for c in content]


def get_badge_from_rucksacks(rucksacks: List[Rucksack]) -> str:
    for item in rucksacks[0].inventory:
        is_in_other_rucksacks = []
        for i, rucksack in enumerate(rucksacks):
            if i == 0:
                continue
            if rucksack.is_item_in_inventory(item):
                is_in_other_rucksacks.append(True)
                continue
            is_in_other_rucksacks.append(False)

        if False in is_in_other_rucksacks:
            continue
        return item
    return ""


if __name__ == '__main__':
    data = get_input_data("./input.txt")
    rucksacks = []
    priority_sum = 0
    badges_priority_sum = 0
    for inventory in data:
        rucksack = Rucksack(inventory)
        rucksacks.append(rucksack)
        priority = rucksack.find_duplicated_item_priority()
        priority_sum += priority
        if len(rucksacks) == 3:
            item = get_badge_from_rucksacks(rucksacks)
            badges_priority_sum += get_item_priority(item)
            rucksacks = []

    print(priority_sum)
    print(badges_priority_sum)
