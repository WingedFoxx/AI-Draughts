def catching_move(self, white):
    moves = [self]
    for i in [-1, 1]:
        if self.isBlack(white.position().add(1, i)):
            if self.isEmpty(white.position().add(2, 2*i)):
                move = [white.position(), white.position().add(2, 2 * i)]
                moves += [catching_move(make_move(self, move), white)]
    return moves

def catching_king(self, white):
    moves = [self]
    for xi in [-1, 1]:
        for yi in [-1, 1]:
            where = white.position().add(yi, xi)
            # Go in that direction, until an occuppied field is found or we reach the end of the board
            while (self.isEmpty(where)):
                where = where.add(yi, xi)
            if self.isBlack(where) and self.isEmpty(where.add(yi, xi)):
                move = [white.position(), white.position().add(yi, xi)
                moves += [catching_king(make_move(self, move), white)]
    return moves
    
        

def possible_moves(self):
    moves = [] # insert the list of moves here
    #catching moves---------------------------------------------------------
    # Iterate over all the white pieces
    for white in self.whites:
        # Consider different cases, depending on whether a piece is a king or not
        if not white.king:
            for i in [-1, 1]:
                if self.isBlack(white.position().add(1, i)):
                    if self.isEmpty(white.position().add(2, 2*i)):
                        move = [white.position(), white.position().add(2, 2 * i)]
                        moves += [catching_move(make_move(self, move), white)]
                            
        else:
            # Iterate over possible directions of movement
            for xi in [-1, 1]:
                for yi in [-1, 1]:
                    where = white.position().add(yi, xi)
                    # Go in that direction, until an occuppied field is found or we reach the end of the board
                    while (self.isEmpty(where)):
                        where = where.add(yi, xi)
                    if self.isBlack(where) and self.isEmpty(where.add(yi, xi)):
                        moves += [catching_king(make_move(self, move), white)]

    #normal moves-------------------------------------------------------------
    # Iterate over all the white pieces
    for white in self.whites:
        for i in [-1, 1]:
            # If a piece is a man, check only if a forward-left or forward-right field is empty
            if self.isEmpty(white.position().add(1, i)):
                moves += [make_move(self, move)]
             # If it's a king, check also if a backward-left or backward-right field is empty
            if white.king and self.isEmpty(white.position().add(-1, i)):
                 moves += [make_move(self, move)]

    return moves
    

    
