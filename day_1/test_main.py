from unittest import TestCase, mock
from main import get_input_data, get_elfs, Elfs, Elf


class Test(TestCase):
    def test_get_input_data(self):
        inventories = get_input_data("./input_test.txt")
        expected_values = [[1, 2, 3, 4], [5, 6, 7, 8], [1]]
        for i, inventory in enumerate(inventories):
            assert inventory == expected_values[
                i], f"Inventory doesn't match, want {expected_values[i]}, got {inventory}"

    @mock.patch("main.get_input_data")
    def test_get_elfs(self, mock_input_data):
        mock_input_data.return_value = [[1, 2], [2, 3]]
        elfs = get_elfs("foo")
        expected_result = Elfs([Elf([1, 2]), Elf([2, 3])])
        for i, elf in enumerate(elfs.elfs):
            exp = expected_result.elfs[i].inventory
            assert elf.inventory == exp, f"Elf inventory doesn't match, want {exp}, got {elf.inventory}"

    def test_get_calories(self):
        elf = Elf([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        inv_calories = elf.get_calories()
        assert inv_calories == 55, f"Calories should be 55, got {inv_calories}"

    def test_get_sorted_calories(self):
        elfs = Elfs([
            Elf([1, 2, 3, 4]),
            Elf([1, 2, 3, 5]),
            Elf([20, 40])
        ])
        expected_result = [60, 11, 10]
        sorted_calories = elfs.get_sorted_calories()
        assert sorted_calories == expected_result, f"List of calories doesn't match, want {expected_result}, got {sorted_calories}"

    def test_get_highest_calories_count(self):
        elfs = Elfs([
            Elf([1, 2, 3, 4]),
            Elf([1, 2, 3, 5]),
            Elf([20, 40])
        ])
        max_calories = elfs.get_highest_calories_count()
        assert max_calories == 60, f"Calories doesn't match, want 60, got {max_calories}"

    def test_get_highest_three_calories_sum(self):
        elfs = Elfs([
            Elf([1, 2, 3, 4]),
            Elf([1, 2, 3, 5]),
            Elf([20, 40]),
            Elf([20, 30]),
            Elf([20, 20]),
        ])
        max_calories = elfs.get_highest_three_calories_sum()
        assert max_calories == 150, f"Calories doesn't match, want 150, got {max_calories}"
