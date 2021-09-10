max_depth = 5 #or something else
def minmax(state, depth):
    if depth == max_depth:
        return heuristic_value(state)
    value = -100000
    for move in state.possible_moves():
        value = max(value, -minmax(make_move(move), depth + 1))
    return value
