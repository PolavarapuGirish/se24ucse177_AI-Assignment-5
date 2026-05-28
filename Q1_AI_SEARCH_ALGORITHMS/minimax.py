from game import PLAYER_X, PLAYER_O

def minimax(game, maximizing):
    result = game.winner()

    if result == PLAYER_X:
        return 1

    if result == PLAYER_O:
        return -1

    if result == 'Draw':
        return 0

    if maximizing:
        best = -1000

        for move in game.available_moves():
            game.make_move(move, PLAYER_X)
            score = minimax(game, False)
            game.undo_move(move)

            best = max(best, score)

        return best

    else:
        best = 1000

        for move in game.available_moves():
            game.make_move(move, PLAYER_O)
            score = minimax(game, True)
            game.undo_move(move)

            best = min(best, score)

        return best

def best_move(game):
    best_score = -1000
    move_choice = None

    for move in game.available_moves():
        game.make_move(move, PLAYER_X)
        score = minimax(game, False)
        game.undo_move(move)

        if score > best_score:
            best_score = score
            move_choice = move

    return move_choice
