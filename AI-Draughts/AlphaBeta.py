def AlphaBeta(self, depth, best, worse):
    if(depth == max_depth):
        return heuristic_value(self)

    if(depth % 2 == 0):
        value = -inf
        for move in self.possible_moves:
            new_value = AlphaBeta(self.make_move(move), depth + 1, best, worse)
            best = max(best, new_value)
            if new_value >= worse:
                return new_value
            value = max(value, new_value)
            
    else:
        value = inf
        for move in self.possible_moves:
            new_value = AlphaBeta(self.make_move(move), depth + 1, best, worse)
            worse = min(worse, new_value)
            if new_value <= best:
                return new_value
            value = min(value, new_value)

    return value
