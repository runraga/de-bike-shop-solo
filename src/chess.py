import re
from abc import ABC, abstractmethod

class Position:
    def __init__(self, rank='A', file=1):
        if not re.match("[A-H]", rank, re.IGNORECASE) or file > 8 or file < 1:
            raise InvalidPositionError("That is not a valid position")
        self.rank = rank
        self.file = file
    def distance_from(self, other_position):
        rank_str = "ABCDEFGH"
        rank_difference = rank_str.index(other_position.rank) - rank_str.index(self.rank)
        file_diference = other_position.file - self.file
        return (rank_difference, file_diference)
    
class Piece(ABC):
    def __init__(self, colour, rank, file):
        self.position = Position(rank, file)
        self.colour = colour
        self.captured = False

    def move_to(self, rank, file):
        valid_moves = self.can_move_to()
        if (rank, file) not in valid_moves:
           raise InvalidMoveError("That piece cannot move to that position")
        else:
            if hasattr(self, "has_moved"):
               self.has_moved = True 
            self.position = Position(rank, file)

    @abstractmethod
    def can_move_to(self):
        pass

    def set_captured(self):
        self.captured = True

class Pawn(Piece):
    def __init__(self, colour,rank,file):
        super().__init__(colour, rank, file)
        self.has_moved = False

    def can_move_to(self):
        if self.has_moved:
            return [(self.position.rank, self.position.file + 1)]
        else:
            return [(self.position.rank, self.position.file + 1),
                    (self.position.rank, self.position.file + 2)]
        
class InvalidPositionError(Exception):
    pass
class InvalidMoveError(Exception):
    pass