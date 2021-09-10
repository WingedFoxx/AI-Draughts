def heuristic_value(self):
    turn = max_depth % 2
    if white_lost(self):
        if turn == 0:
            return -inf
        return inf

    value = 0
    if self.whites.len > self.blacks.len:
        if turn == 0:
            value += self.whites.len - self.blacks.len
        else:
            value -= self.whites.len - self.blacks.len
    

    return value
