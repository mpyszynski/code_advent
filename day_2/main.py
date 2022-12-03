from typing import List
from dataclasses import dataclass
from enum import Enum


@dataclass
class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


@dataclass
class Game:
    opponent_move: Move
    player_move: Move

    def match(self) -> int:
        if self.player_move.value == Move.ROCK.value:
            return self.rock_match()
        if self.player_move.value == Move.PAPER.value:
            return self.paper_match()
        if self.player_move.value == Move.SCISSORS.value:
            return self.scissors_match()

    def rock_match(self) -> int:
        if self.opponent_move.value == Move.PAPER.value:
            return 0
        if self.opponent_move.value == Move.SCISSORS.value:
            return 6
        return 3

    def paper_match(self) -> int:
        if self.opponent_move.value == Move.ROCK.value:
            return 6
        if self.opponent_move.value == Move.SCISSORS.value:
            return 0
        return 3

    def scissors_match(self) -> int:
        if self.opponent_move.value == Move.ROCK.value:
            return 0
        if self.opponent_move.value == Move.PAPER.value:
            return 6
        return 3


def read_input_file(source: str) -> List[List[str]]:
    f = open(source, "r")
    input_values = []
    for line in f:
        values = line.strip().split(" ")
        input_values.append([values[0], values[1]])
    f.close()
    return input_values


def new_move(val: str) -> Move:
    if val == "A" or val == "X":
        return Move.ROCK
    if val == "B" or val == "Y":
        return Move.PAPER
    if val == "C" or val == "Z":
        return Move.SCISSORS


def new_dynamic_move(opp_move: Move, player_move: str) -> Move:
    if player_move == "X":
        return find_move(opp_move, 0)
    if player_move == "Y":
        return find_move(opp_move, 3)
    return find_move(opp_move, 6)


def find_move(move_one: Move, result: int) -> Move:
    possible_moves = [Move.ROCK, Move.PAPER, Move.SCISSORS]
    for move in possible_moves:
        game = Game(move_one, move)
        if game.match() == result:
            return move


if __name__ == '__main__':
    inputs = read_input_file("input.txt")
    standard_games_count = 0
    dynamic_moves_games_count = 0
    for ipt in inputs:
        opponent_move = new_move(ipt[0])
        standard_game = Game(opponent_move, new_move(ipt[1]))
        standard_games_count += standard_game.match() + standard_game.player_move.value
        dynamic_move_game = Game(opponent_move, new_dynamic_move(opponent_move, ipt[1]))
        dynamic_moves_games_count += dynamic_move_game.match() + dynamic_move_game.player_move.value

    print(f"Standard games count {standard_games_count}")
    print(f"Dynamic moves games count {dynamic_moves_games_count}")
