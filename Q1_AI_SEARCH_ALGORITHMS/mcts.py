import random
import math
from copy import deepcopy
from game import PLAYER_X, PLAYER_O

class Node:
    def __init__(self, game, parent=None, move=None):
        self.game = deepcopy(game)
        self.parent = parent
        self.move = move
        self.children = []
        self.wins = 0
        self.visits = 0

    def fully_expanded(self):
        return len(self.children) == len(self.game.available_moves())

    def best_child(self, c=1.41):
        choices = []

        for child in self.children:
            uct = (
                (child.wins / child.visits) +
                c * math.sqrt(math.log(self.visits) / child.visits)
            )

            choices.append((uct, child))

        return max(choices, key=lambda x: x[0])[1]

def random_playout(game, player):
    current = player

    while game.winner() is None:
        move = random.choice(game.available_moves())
        game.make_move(move, current)

        if current == PLAYER_X:
            current = PLAYER_O
        else:
            current = PLAYER_X

    return game.winner()

def mcts(root_game, simulations=1000):
    root = Node(root_game)

    for _ in range(simulations):
        node = root

        while node.children and node.fully_expanded():
            node = node.best_child()

        if node.game.winner() is None:
            tried_moves = [child.move for child in node.children]

            possible_moves = [
                move for move in node.game.available_moves()
                if move not in tried_moves
            ]

            if possible_moves:
                move = random.choice(possible_moves)

                new_game = deepcopy(node.game)

                if new_game.board.count(PLAYER_X) == new_game.board.count(PLAYER_O):
                    player = PLAYER_X
                else:
                    player = PLAYER_O

                new_game.make_move(move, player)

                child = Node(new_game, node, move)

                node.children.append(child)

                node = child

        simulation_game = deepcopy(node.game)

        if simulation_game.board.count(PLAYER_X) == simulation_game.board.count(PLAYER_O):
            player = PLAYER_X
        else:
            player = PLAYER_O

        result = random_playout(simulation_game, player)

        while node:
            node.visits += 1

            if result == PLAYER_X:
                node.wins += 1

            node = node.parent

    best = max(root.children, key=lambda child: child.visits)

    return best.move
