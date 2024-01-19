from src.chess import *
import pytest

def test_position_has_rank_and_file_property():
    position = Position()
    assert hasattr(position, 'rank')
    assert hasattr(position, 'file')

def test_raises_error_for_invalid_position():
    with pytest.raises(
        InvalidPositionError,
        match = "That is not a valid position"
    ):
        Position("J", 8)
    with pytest.raises(
        InvalidPositionError,
        match = "That is not a valid position"
    ):
        Position("A", 10)
    
def test_distance_from_returns_0_0_if_positions_are_equal():
    position1 = Position()
    position2 = Position()
    result = position1.distance_from(position2)
    assert result == (0,0)

def test_distance_from_returns_correct_distance():
    position1 = Position()
    position2 = Position("B", 2)
    result = position1.distance_from(position2)
    assert result == (1,1)

    position3 = Position("C", 3)
    position4 = Position("B", 2)
    result = position3.distance_from(position4)
    assert result == (-1,-1)

def test_Piece_class_has_colour_and_Position():
    piece = Pawn("white", "A", 1)
    assert hasattr(piece, 'colour')
    assert hasattr(piece, 'position')

def test_moveTo_update_position_correctly():
     piece = Pawn("white", "A", 1)
     piece.move_to("A", 2)
     result = piece.position
     assert result.rank == "A"
     assert result.file == 2

def test_piece_class_has_captured_property_of_type_boolean():
    piece = Pawn("white", "A", 1)
    assert hasattr(piece, "captured")
    assert type(piece.captured) is bool

def test_piece_class_can_set_captured_property():
    piece = Pawn("white", "A", 1)
    piece.set_captured()
    assert piece.captured == True

def test_pawn_has_has_moved_property_of_type_boolean():
    piece = Pawn("white", "A", 1)
    assert hasattr(piece, "has_moved")
    assert type(piece.has_moved) is bool

def test_pawn_can_move_to_return_corrent_list_of_valid_moves():
    pawn = Pawn("white", "A", 2)
    expected = [("A", 3), ("A", 4)]
    result = pawn.can_move_to()
    assert result == expected

def test_move_to_method_compares_valid_moves_with_parameters_raise_error_if_invalid_move():
    with pytest.raises(
        InvalidMoveError,
        match = "That piece cannot move to that position"
    ):
    
        pawn = Pawn("white", "A", 2)
        pawn.move_to("H", 5)

def test_move_to_method_for_pawn_updates_has_moved_to_true():  
    pawn = Pawn("white", "A", 2)
    pawn.move_to("A", 3)
    assert pawn.has_moved == True

def test_can_move_to_method_for_pawn_only_has_one_valid_moved_if_already_moved():  
    pawn = Pawn("white", "A", 2)
    pawn.move_to("A", 3)
    result = pawn.can_move_to()
    expected = [("A", 4)]
    assert result == expected
