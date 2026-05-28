from game import PLAYER_X, PLAYER_O, EMPTY

def heuristic(game):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    score = 0

    for combo in wins:
        values = [game.board[i] for i in combo]

        if values.count(PLAYER_X) == 2 and values.count(EMPTY) == 1:
            score += 5

        if values.count(PLAYER_O) == 2 and values.count(EMPTY) == 1:
            score -= 5

    return score

def alphabeta(game, depth, alpha, beta, maximizing):
    result = game.winner()

    if result == PLAYER_X:
        return 100

    if result == PLAYER_O:
        return -100

    if result == 'Draw':
        return 0

    if depth == 0:
        return heuristic(game)

    if maximizing:
        value = -1000

        for move in game.available_moves():
            game.make_move(move, PLAYER_X)

            value = max(
                value,
                alphabeta(game, depth - 1, alpha, beta, False)
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
                alphabeta(game, depth - 1, alpha, beta, True)
            )

            game.undo_move(move)

            beta = min(beta, value)

            if beta <= alpha:
                break

        return value

def best_move(game, depth):
    best_score = -1000
    move_choice = None

    for move in game.available_moves():
        game.make_move(move, PLAYER_X)

        score = alphabeta(
            game,
            depth,
            -1000,
            1000,
            False
        )

        game.undo_move(move)

        if score > best_score:
            best_score = score
            move_choice = move

    return move_choice
