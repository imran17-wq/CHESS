WHITE = 0
BLACK = 1

PAWN = 0
KNIGHT = 1
BISHOP = 2
ROOK = 3
QUEEN = 4
KING = 5
pieces = {
    (WHITE, PAWN): 0,
    (WHITE, KNIGHT): 0,
    (WHITE, BISHOP): 0,
    (WHITE, ROOK): 0,
    (WHITE, QUEEN): 0,
    (WHITE, KING): 0,

    (BLACK, PAWN): 0,
    (BLACK, KNIGHT): 0,
    (BLACK, BISHOP): 0,
    (BLACK, ROOK): 0,
    (BLACK, QUEEN): 0,
    (BLACK, KING): 0,
}
def setup_starting_position():
    for key in pieces:
        pieces[key] = 0
    for square in range(48, 56):
        pieces[(WHITE, PAWN)] |= 1 << square
    for square in range(8, 16):
        pieces[(BLACK, PAWN)] |= 1 << square
    pieces[(WHITE, ROOK)]   |= 1 << 56
    pieces[(WHITE, KNIGHT)] |= 1 << 57
    pieces[(WHITE, BISHOP)] |= 1 << 58
    pieces[(WHITE, QUEEN)]  |= 1 << 59
    pieces[(WHITE, KING)]   |= 1 << 60
    pieces[(WHITE, BISHOP)] |= 1 << 61
    pieces[(WHITE, KNIGHT)] |= 1 << 62
    pieces[(WHITE, ROOK)]   |= 1 << 63

    pieces[(BLACK, ROOK)]   |= 1 << 0
    pieces[(BLACK, KNIGHT)] |= 1 << 1
    pieces[(BLACK, BISHOP)] |= 1 << 2
    pieces[(BLACK, QUEEN)]  |= 1 << 3
    pieces[(BLACK, KING)]   |= 1 << 4
    pieces[(BLACK, BISHOP)] |= 1 << 5
    pieces[(BLACK, KNIGHT)] |= 1 << 6
    pieces[(BLACK, ROOK)]   |= 1 << 7
def print_bitboard(bb):
    for row in range(8):
        for col in range(8):
            square = row * 8 + col
            if bb & (1 << square):
                print("1", end=" ")
            else:
                print(".", end=" ")
        print()
setup_starting_position()
print("White Pawns:")
print_bitboard(pieces[(WHITE, PAWN)])
print()
print("Black Pawns:")
print_bitboard(pieces[(BLACK, PAWN)])
print()
print("White King:")
print_bitboard(pieces[(WHITE, KING)])
print()
print("Black King:")
print_bitboard(pieces[(BLACK, KING)])
def get_occupancy():
    white = 0
    black = 0
    for (color, piece_type), bitboard in pieces.items():
        if color == WHITE:
            white |= bitboard
        else:
            black |= bitboard
    occupied = white | black
    return white, black, occupied
setup_starting_position()
white_occupancy, black_occupancy, occupancy = get_occupancy()
print("White occupancy:")
print_bitboard(white_occupancy)
print()
print("Black occupancy:")
print_bitboard(black_occupancy)
print()
print("All occupied:")
print_bitboard(occupancy)
def knight_moves(square, color):

    row = square // 8
    col = square % 8

    moves = []

    knight_jumps = [
        (-2, -1),
        (-2, +1),
        (-1, -2),
        (-1, +2),
        (+1, -2),
        (+1, +2),
        (+2, -1),
        (+2, +1)
    ]

    white, black, occupied = get_occupancy()

    for row_change, col_change in knight_jumps:

        new_row = row + row_change
        new_col = col + col_change

        # Is the new square still on the board?
        if 0 <= new_row < 8 and 0 <= new_col < 8:

            new_square = new_row * 8 + new_col

            # Don't move onto our own piece
            if color == WHITE:
                if white & (1 << new_square):
                    continue

            else:
                if black & (1 << new_square):
                    continue

            moves.append(new_square)

    return moves
def get_piece_at(square):
    for (color, piece_type), bitboard in pieces.items():
        if bitboard & (1 << square):
            return color, piece_type
    return None
def print_board():
    symbols = {
        (WHITE, PAWN): "♙",
        (WHITE, KNIGHT): "♘",
        (WHITE, BISHOP): "♗",
        (WHITE, ROOK): "♖",
        (WHITE, QUEEN): "♕",
        (WHITE, KING): "♔",

        (BLACK, PAWN): "♟",
        (BLACK, KNIGHT): "♞",
        (BLACK, BISHOP): "♝",
        (BLACK, ROOK): "♜",
        (BLACK, QUEEN): "♛",
        (BLACK, KING): "♚",
    }
    for row in range(8):
        print(8 - row, end="  ")
        for col in range(8):
            square = row * 8 + col
            piece = get_piece_at(square)
            if piece is None:
                print(".", end=" ")
            else:
                print(symbols[piece], end=" ")
        print()
    print()
    print("   a b c d e f g h")
setup_starting_position()
print_board()