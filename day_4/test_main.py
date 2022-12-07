from unittest import TestCase
from main import Assignment, do_rooms_overlap, get_input_data, get_rooms_list


class TestAssigment(TestCase):
    def test_is_assignment_overlapping(self):
        test_cases = [
            {"rooms_one": [6], "rooms_two": [4, 5, 6], "exp_res": True},
            {"rooms_one": [4, 5, 6], "rooms_two": [6], "exp_res": True},
            {"rooms_one": [2, 3, 4, 5, 6], "rooms_two": [6, 7, 8, 9, 10], "exp_res": False},
            {"rooms_one": [2, 3, 4, 5, 6, 7, 8], "rooms_two": [3, 4, 5, 6, 7], "exp_res": True},
        ]

        for case in test_cases:
            assigment = Assignment(case["rooms_one"], case["rooms_two"])
            res = assigment.is_assignment_overlapping()
            assert res == case["exp_res"], f"Unexpected result, wanted {case['exp_res']}, got {res}"

    def test_is_room_overlapping(self):
        test_cases = [
            {"rooms_one": [6], "rooms_two": [4, 5, 6], "exp_res": True},
            {"rooms_one": [4, 5, 6], "rooms_two": [6], "exp_res": True},
            {"rooms_one": [2, 3, 4, 5, 6], "rooms_two": [6, 7, 8, 9, 10], "exp_res": True},
            {"rooms_one": [2, 3, 4, 5, 6, 7, 8], "rooms_two": [3, 4, 5, 6, 7], "exp_res": True},
            {"rooms_one": [1, 2], "rooms_two": [3, 4], "exp_res": False},
            {"rooms_one": [2, 3, 4, 5, 6, 7, 8], "rooms_two": [9, 10, 11, 12], "exp_res": False},
        ]

        for case in test_cases:
            assignment = Assignment(case["rooms_one"], case["rooms_two"])
            res = assignment.is_room_overlapping()
            assert res == case["exp_res"], f"Unexpected result, wanted {case['exp_res']}, got {res}"

    def test_do_rooms_overlap(self):
        test_cases = [
            {"rooms_one": [6], "rooms_two": [4, 5, 6], "exp_res": True},
            {"rooms_one": [4, 5, 6], "rooms_two": [6], "exp_res": False},
            {"rooms_one": [2, 3, 4, 5, 6], "rooms_two": [6, 7, 8, 9, 10], "exp_res": False},
            {"rooms_one": [2, 3, 4, 5, 6, 7, 8], "rooms_two": [3, 4, 5, 6, 7], "exp_res": False},
        ]

        for case in test_cases:
            res = do_rooms_overlap(case["rooms_one"], case["rooms_two"])
            assert res == case["exp_res"], f"Unexpected result, wanted {case['exp_res']}, got {res}"

    def test_get_input_data(self):
        data = get_input_data("./input_test.txt")
        assert data == [["21-81", "20-96"], ["14-80", "14-79"], ["87-89", "7-88"], ["82-93", "44-82"]]

    def test_get_rooms_list(self):
        rooms = get_rooms_list(1, 5)
        exp_res = [1, 2, 3, 4, 5]
        assert rooms == exp_res, f"Unexpected result, wanted {exp_res}, got {rooms}"
