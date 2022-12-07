from dataclasses import dataclass
from typing import List


@dataclass
class Assignment:
    elf_one_rooms: List[int]
    elf_two_rooms: List[int]

    def is_assignment_overlapping(self) -> bool:
        if do_rooms_overlap(self.elf_one_rooms, self.elf_two_rooms):
            return True

        return do_rooms_overlap(self.elf_two_rooms, self.elf_one_rooms)

    def is_room_overlapping(self) -> bool:
        for room in self.elf_one_rooms:
            if room in self.elf_two_rooms:
                return True


def do_rooms_overlap(r1: List[int], r2: List[int]) -> bool:
    are_overlapping = False
    for room in r1:
        if room not in r2:
            are_overlapping = False
            break
        are_overlapping = True
    return are_overlapping


def get_input_data(source: str) -> List[List[str]]:
    f = open(source, "r")
    data = []
    for line in f:
        rooms = line.strip().split(",")
        data.append(rooms)
    f.close()
    return data


def new_assignment(rooms: List[str]) -> Assignment:
    rooms_elf_one_spread = rooms[0].split("-")
    rooms_elf_two_spread = rooms[1].split("-")
    return Assignment(
        elf_one_rooms=get_rooms_list(int(rooms_elf_one_spread[0]), int(rooms_elf_one_spread[1])),
        elf_two_rooms=get_rooms_list(int(rooms_elf_two_spread[0]), int(rooms_elf_two_spread[1])),
    )


def get_rooms_list(start: int, end: int) -> List[int]:
    rooms = []
    [rooms.append(room) for room in range(start, end + 1)]
    return rooms


def main():
    data = get_input_data("./input.txt")
    assignments_overlapping_count = 0
    rooms_overlapping_count = 0
    for rooms in data:
        assignment = new_assignment(rooms)
        if assignment.is_assignment_overlapping():
            assignments_overlapping_count += 1
        if assignment.is_room_overlapping():
            rooms_overlapping_count += 1
    print(f"Overlapping assignments {assignments_overlapping_count}")
    print(f"Overlapping rooms {rooms_overlapping_count}")


if __name__ == '__main__':
    main()
