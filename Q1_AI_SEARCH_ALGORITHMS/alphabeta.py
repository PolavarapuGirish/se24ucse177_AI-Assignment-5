from game import PLAYER_X, PLAYER_O

def alphabeta(game, alpha, beta, maximizing):
    result = game.winner()

    if result == PLAYER_X:
        return 1

    if result == PLAYER_O:
        return -1

    if result == 'Draw':
        return 0

    if maximizing:
        value = -1000

        for move in game.available_moves():
            game.make_move(move, PLAYER_X)

            value = max(
                value,
                alphabeta(game, alpha, beta, False)
            )

            game.undo_move(move)

            alpha = max(alpha, value)

            if beta <= alpha:
                break

        return value

    else:
        value = 1000

        for move in game.available_moves():
            game.make_move(move, PLAYER_O)

            value = min(
                value,
                alphabeta(game, alpha, beta, True)
            )

            game.undo_move(move)

            beta = min(beta, value)

            if beta <= alpha:
                break

        return value

def best_move(game):
    best_score = -1000
    move_choice = None

    for move in game.available_moves():
        game.make_move(move, PLAYER_X)

        score = alphabeta(
            game,
            -1000,
            1000,
            False
        )

        game.undo_move(move)

        if score > best_score:
            best_score = score
            move_choice = move

    return move_choice
