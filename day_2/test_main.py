from unittest import TestCase
from main import Game, Move, read_input_file, find_move


class TestGame(TestCase):
    def test_scissors_match(self):
        test_cases = [
            {"move": Move.ROCK, "exp_val": 0},
            {"move": Move.PAPER, "exp_val": 6},
            {"move": Move.SCISSORS, "exp_val": 3},
        ]
        for test in test_cases:
            game = Game(test["move"], Move.SCISSORS)
            match = game.scissors_match()
            assert match == test["exp_val"], f"Unexpected value, wanted {test['exp_val']}, got {match}"

    def test_paper_match(self):
        test_cases = [
            {"move": Move.ROCK, "exp_val": 6},
            {"move": Move.PAPER, "exp_val": 3},
            {"move": Move.SCISSORS, "exp_val": 0},
        ]
        for test in test_cases:
            game = Game(test["move"], Move.PAPER)
            match = game.paper_match()
            assert match == test["exp_val"], f"Unexpected value, wanted {test['exp_val']}, got {match}"

    def test_rock_match(self):
        test_cases = [
            {"move": Move.ROCK, "exp_val": 3},
            {"move": Move.PAPER, "exp_val": 0},
            {"move": Move.SCISSORS, "exp_val": 6},
        ]
        for test in test_cases:
            game = Game(test["move"], Move.ROCK)
            match = game.rock_match()
            assert match == test["exp_val"], f"Unexpected value, wanted {test['exp_val']}, got {match}"

    def test_matches(self):
        test_cases = [
            {"opponent_move": Move.ROCK, "player_move": Move.ROCK, "exp_val": 3},
            {"opponent_move": Move.ROCK, "player_move": Move.PAPER, "exp_val": 6},
            {"opponent_move": Move.ROCK, "player_move": Move.SCISSORS, "exp_val": 0},
            {"opponent_move": Move.PAPER, "player_move": Move.ROCK, "exp_val": 0},
            {"opponent_move": Move.PAPER, "player_move": Move.PAPER, "exp_val": 3},
            {"opponent_move": Move.PAPER, "player_move": Move.SCISSORS, "exp_val": 6},
            {"opponent_move": Move.SCISSORS, "player_move": Move.ROCK, "exp_val": 6},
            {"opponent_move": Move.SCISSORS, "player_move": Move.PAPER, "exp_val": 0},
            {"opponent_move": Move.SCISSORS, "player_move": Move.SCISSORS, "exp_val": 3},
        ]
        for test in test_cases:
            game = Game(test["opponent_move"], test["player_move"])
            match = game.match()
            assert match == test["exp_val"], f"Unexpected value, wanted {test['exp_val']}, got {match}"

    def test_read_input_file(self):
        values = read_input_file("./input_test.txt")
        expected_values = [
            ["C", "Y"],
            ["C", "Y"],
            ["B", "Y"],
            ["A", "Z"],
        ]
        for i, value in enumerate(values):
            assert value[0] == expected_values[i][
                0], f"Unexpected value, wanted {value[0]}, got {expected_values[i][0]}, loop {i}"
            assert value[1] == expected_values[i][
                1], f"Unexpected value, wanted {value[1]}, got {expected_values[i][1]}, loop {i}"

    def test_find_move(self):
        test_cases = [
            {"opp_move": Move.ROCK, "result": 0, "exp_res": Move.PAPER},
            {"opp_move": Move.ROCK, "result": 3, "exp_res": Move.ROCK},
            {"opp_move": Move.ROCK, "result": 6, "exp_res": Move.SCISSORS},
            {"opp_move": Move.PAPER, "result": 0, "exp_res": Move.SCISSORS},
            {"opp_move": Move.PAPER, "result": 3, "exp_res": Move.PAPER},
            {"opp_move": Move.PAPER, "result": 6, "exp_res": Move.SCISSORS},
            {"opp_move": Move.SCISSORS, "result": 0, "exp_res": Move.ROCK},
            {"opp_move": Move.SCISSORS, "result": 3, "exp_res": Move.SCISSORS},
            {"opp_move": Move.SCISSORS, "result": 6, "exp_res": Move.PAPER},
        ]

        for case in test_cases:
            move = find_move(case["opp_move"], case["result"])
            assert move == case["exp_res"], f"Unexpected result, wanted {case['exp_res']}, got {move}"
