from dataclasses import dataclass
from typing import List


@dataclass
class Elf:
    inventory: List[int]

    def get_calories(self) -> int:
        return sum(self.inventory)


@dataclass
class Elfs:
    elfs: List[Elf]

    def get_sorted_calories(self) -> List[int]:
        calories_list = []
        for elf in self.elfs:
            calories_list.append(elf.get_calories())
        calories_list.sort(reverse=True)
        return calories_list

    def get_highest_calories_count(self) -> int:
        return self.get_sorted_calories()[0]

    def get_highest_three_calories_sum(self) -> int:
        calories_list = self.get_sorted_calories()
        return sum(calories_list[:3])


def get_input_data(source: str) -> List[List[int]]:
    f = open(source, "r")
    inventories = []
    inventory = []
    for line in f:
        if line != "\n":
            inventory.append(int(line))
        else:
            inventories.append(inventory)
            inventory = []
            continue
    f.close()
    return inventories


def get_elfs(source: str) -> Elfs:
    elfs = []
    inventories = get_input_data(source)
    for inv in inventories:
        elfs.append(Elf(inv))
    return Elfs(elfs)


if __name__ == '__main__':
    elfs = get_elfs("./input.txt")
    max_calories = elfs.get_highest_calories_count()
    print(f"Maximum amount of calories one elf has is {max_calories}")
    max_three_elfs_calories = elfs.get_highest_three_calories_sum()
    print(f"Maximum amount of calories from three elfs is {max_three_elfs_calories}")
