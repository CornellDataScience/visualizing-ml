# A declaration of all the constants used in this project

FEN_STARTING_POSITION = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
FEN_EMPTY = '4k3/8/8/8/8/8/8/4K3 b - - 0 1'
FEN_1E4 = 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1'
FEN_IMMORTAL_GAME = 'r1bk2nr/p2p1pNp/n2B1Q2/1p1NP2P/6P1/3P4/P1P1K3/q5b1 w - - 0 1'


BOARD_SIZE = 700 # pixel width and height of chessboard.png
BOARD_OFFSET = 30 # pixels of margin between board and edge in chessboard.png
SQUARE_SIZE = 80 # Each square of our chess board is 80x80 pixels


# Board size? idk where we might need this
NUMROWS = 8
NUMCOLS = 8

# Numerical codes for the type of piece
EMPTY = 0

LTKING = 1
LTQUEEN = 2
LTROOK = 3
LTBISHOP = 4
LTKNIGHT = 5
LTPAWN = 6

DKKING = 7
DKQUEEN = 8
DKROOK = 9
DKBISHOP = 10
DKKNIGHT = 11
DKPAWN = 12

# Paths for all the images used in this project
PATH_CHESSBOARD = r'imgs/chessboard_nbkgd.png'
PATH_LTKING = r'imgs/king_light.png'
PATH_DKKING = r'imgs/king_dark.png'
PATH_LTQUEEN = r'imgs/queen_light.png'
PATH_DKQUEEN = r'imgs/queen_dark.png'
PATH_LTROOK = r'imgs/rook_light.png'
PATH_DKROOK = r'imgs/rook_dark.png'
PATH_LTBISHOP = r'imgs/bishop_light.png'
PATH_DKBISHOP = r'imgs/bishop_dark.png'
PATH_LTKNIGHT = r'imgs/knight_light.png'
PATH_DKKNIGHT = r'imgs/knight_dark.png'
PATH_LTPAWN = r'imgs/pawn_light.png'
PATH_DKPAWN = r'imgs/pawn_dark.png'
PATH_LTUNICORN = r'imgs/unicorn_light.png'
PATH_DKUNICORN = r'imgs/unicorn_dark.png'

PATH_AQUA_HIGHLIGHT = r'imgs/aqua_highlight.png'
PATH_GREEN_HIGHLIGHT = r'imgs/green_highlight.png'
PATH_RED_HIGHLIGHT = r'imgs/red_highlight.png'
PATH_YELLOW_HIGHLIGHT = r'imgs/yellow_highlight.png'
PATH_MAGENTA_HIGHLIGHT = r'imgs/magenta_highlight.png'