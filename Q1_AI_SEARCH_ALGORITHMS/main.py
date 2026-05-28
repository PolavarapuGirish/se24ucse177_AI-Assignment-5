from game import TicTacToe
from minimax import best_move as minimax_move
from alphabeta import best_move as alphabeta_move
from heuristic_alphabeta import best_move as heuristic_move
from mcts import mcts

game = TicTacToe()

print("Initial Board")
game.print_board()

print()

print("Minimax Move:", minimax_move(game))

print("Alpha Beta Move:", alphabeta_move(game))

print("Heuristic Alpha Beta Move:", heuristic_move(game, 3))

print("MCTS Move:", mcts(game, 500))
