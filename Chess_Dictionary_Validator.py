def isValidChessBoard(board):
    """Validate counts and location of pieces on board"""

    # Define pieces and colors
    pieces = ['king', 'queen', 'rook', 'knight', 'bishop', 'pawn']
    colors = ['b', 'w']
    # Set of all chess pieces
    all_pieces = set(color + piece for piece in pieces for color in colors)

    # Define valid range for count of chess pieces by type (low, high) tuples
    valid_counts = {'king': (1, 1),
                    'queen': (0, 1),
                    'rook': (0, 2),
                    'bishop': (0, 2),
                    'knight': (0, 2),
                    'pawn': (0, 8)}

    # Get count of pieces on the board
    piece_cnt = {}
    for v in board.values():
        if v in all_pieces:
            piece_cnt.setdefault(v, 0)
            piece_cnt[v] += 1

    # Check if there are a valid number of pieces
    for piece in all_pieces:
        cnt = piece_cnt.get(piece, 0)
        lo, hi = valid_counts[piece[1:]]
        if not lo <= cnt <= hi:  # Count needs to be between lo and hi
            if lo != hi:
                print(f"There should between {lo} and {hi} {piece} but there are {cnt}")
            else:
                print(f"There should be {lo} {piece} but there are {cnt})")
            return False

    # Check if locations are valid
    for location in board.keys():
        row = int(location[:1])
        column = location[1:]
        if not ((1 <= row <= 8) and ('a' <= column <= "h")):
            print(f"Invaid to have {board[location]} at postion {location}")
            return False

    # Check if all pieces have valid names
    for loc, piece in board.items():
        if piece:
            if not piece in all_pieces:
                print(f"{piece} is not a valid chess piece at postion {loc}")
                return False

    return True
board = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
'5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
'1f': '','2f': '','3f': '','4f': '','5f': '','6f': '','7f': '','8f': '',
'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
'1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': '',}

print(isValidChessBoard(board))