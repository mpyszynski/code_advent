from unittest import TestCase
from main import Rucksack, get_badge_from_rucksacks, get_item_priority, get_input_data


class Test(TestCase):
    def test_get_badge_from_rucksacks(self):
        rucksacks = [
            Rucksack("DddBHCmfWCBTDBHTHfMpzhzpJJMJsFrGrz"),
            Rucksack("tPVPmbnttjPnZvSvSbnmZPZPNpNGMpJNzzNrGJpvhsshMpFs"),
            Rucksack("DddBHCmfWCBTDBHTHfMpzhzpJJMJsFrGrz"),
            Rucksack("mwnZcbmmStbVtVjbZVlcLTBlcLCRHRDWCWWW"),
        ]
        item = get_badge_from_rucksacks(rucksacks)
        assert item == "m"

    def test_find_duplicated_item(self):
        r = Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
        item = r.find_duplicated_item()
        assert item == "p"

    def test_find_duplicated_item_priority(self):
        r = Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
        priority = r.find_duplicated_item_priority()
        assert priority == 16

    def test_is_item_in_inventory(self):
        r = Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
        test_cases = [
            {"exp_res": False, "item": "Z"},
            {"exp_res": True, "item": "p"},
        ]
        for case in test_cases:
            is_in_inventory = r.is_item_in_inventory(case["item"])
            assert is_in_inventory == case["exp_res"]

    def test_get_item_priority(self):
        test_cases = [
            {"item": "p", "exp_res": 16},
            {"item": "L", "exp_res": 38},
        ]
        for case in test_cases:
            p = get_item_priority(case["item"])
            assert p == case["exp_res"]

    def test_get_input_data(self):
        content = get_input_data("./input_test.txt")
        print(content)
        assert content == ["vGFhvGvvSdfwqhqvmCPnlFPnCNPcCFcWcr", "ZbWZDMgsTHsrNNLJcJnsJl"]
