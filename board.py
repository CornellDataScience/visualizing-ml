import tkinter as tk
from PIL import Image, ImageTk
import random

# base window
root = tk.Tk()
root.title("Visualizing ML")
root.geometry("1000x1000")

global blackSquares
global whiteSquares
white_pieces = []
black_pieces = []


def labels_top():
    top_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    count = 1
    for label in top_letters:
        label = tk.Label(root, text=label)
        label.grid(column=count, row=0)
        count += 1


def make_board():
    blackSquares = []
    blackSquares += range(0, 32)

    whiteSquares = []
    whiteSquares += range(0, 32)

    for var in blackSquares:
        ind = blackSquares.index(var)
        blackSquares[ind] = tk.Canvas(
            root, width=80, height=80, border=0, bg="blue4", cursor="hand2")

    for var in whiteSquares:
        ind = whiteSquares.index(var)
        whiteSquares[ind] = tk.Canvas(
            root, width=80, height=80, border=0, bg="navajo white", cursor="hand2")

    return blackSquares, whiteSquares


def position_board(blackSquares, whiteSquares):
    bCol = 0
    wCol = -1
    for num in range(0, 4):
        bCol += 2
        wCol += 2
        blackSquares[num].grid(column=bCol, row=1)
        whiteSquares[num].grid(column=wCol, row=1)

    bCol = -1
    wCol = 0
    for num in range(4, 8):
        bCol += 2
        wCol += 2
        blackSquares[num].grid(column=bCol, row=2)
        whiteSquares[num].grid(column=wCol, row=2)

    bCol = 0
    wCol = -1
    for num in range(8, 12):
        bCol += 2
        wCol += 2
        blackSquares[num].grid(column=bCol, row=3)
        whiteSquares[num].grid(column=wCol, row=3)

    bCol = -1
    wCol = 0
    for num in range(12, 16):
        bCol += 2
        wCol += 2
        blackSquares[num].grid(column=bCol, row=4)
        whiteSquares[num].grid(column=wCol, row=4)

    bCol = 0
    wCol = -1
    for num in range(16, 20):
        bCol += 2
        wCol += 2
        blackSquares[num].grid(column=bCol, row=5)
        whiteSquares[num].grid(column=wCol, row=5)

    bCol = -1
    wCol = 0
    for num in range(20, 24):
        bCol += 2
        wCol += 2
        blackSquares[num].grid(column=bCol, row=6)
        whiteSquares[num].grid(column=wCol, row=6)

    bCol = 0
    wCol = -1
    for num in range(24, 28):
        bCol += 2
        wCol += 2
        blackSquares[num].grid(column=bCol, row=7)
        whiteSquares[num].grid(column=wCol, row=7)

    bCol = -1
    wCol = 0
    for num in range(28, 32):
        bCol += 2
        wCol += 2
        blackSquares[num].grid(column=bCol, row=8)
        whiteSquares[num].grid(column=wCol, row=8)

    board = []
    for num in range(0, 4):
        board.append(whiteSquares[num])
        board.append(blackSquares[num])
    for num in range(4, 8):
        board.append(blackSquares[num])
        board.append(whiteSquares[num])
    for num in range(8, 12):
        board.append(whiteSquares[num])
        board.append(blackSquares[num])
    for num in range(12, 16):
        board.append(blackSquares[num])
        board.append(whiteSquares[num])
    for num in range(16, 20):
        board.append(whiteSquares[num])
        board.append(blackSquares[num])
    for num in range(20, 24):
        board.append(blackSquares[num])
        board.append(whiteSquares[num])
    for num in range(24, 28):
        board.append(whiteSquares[num])
        board.append(blackSquares[num])
    for num in range(28, 32):
        board.append(blackSquares[num])
        board.append(whiteSquares[num])
    return board


''' this is used to store the position of a piece, but we can change this
later to match the FEN strings'''

board_spaces = []
for x in range(0, 64):
    board_spaces.append("")

#  finsih this up so we can actually use the set of white_pieces and black_pieces
# for the starting position

'''class Piece():
        def _init_ (self, color, set):
                self.color = color
                self.set = set.append(self)
'''

# pawn


class Pawn():
    black_pawn = ImageTk.PhotoImage(Image.open("./Images/black_pawn.png"))
    white_pawn = ImageTk.PhotoImage(Image.open("./Images/white_pawn.png"))


class Knight():
    black_knight = ImageTk.PhotoImage(Image.open("./Images/black_knight.png"))
    white_knight = ImageTk.PhotoImage(Image.open("./Images/white_knight.png"))


class Bishop():
    black_bishop = ImageTk.PhotoImage(Image.open("./Images/black_bishop.png"))
    white_bishop = ImageTk.PhotoImage(Image.open("./Images/white_bishop.png"))


class Rook():
    black_rook = ImageTk.PhotoImage(Image.open("./Images/black_rook.png"))
    white_rook = ImageTk.PhotoImage(Image.open("./Images/white_rook.png"))


class Queen():
    black_rook = ImageTk.PhotoImage(Image.open("./Images/black_queen.png"))
    white_rook = ImageTk.PhotoImage(Image.open("./Images/white_queen.png"))


class King():
    black_king = ImageTk.PhotoImage(Image.open("./Images/black_king.png"))
    white_king = ImageTk.PhotoImage(Image.open("./Images/white_king.png"))


def starting_position(board_spaces, board, black_pieces, white_pieces):
    for num in range(0, 16):
        piece = black_pieces[num]
        board_spaces[num] = piece
        display = black_pieces[num].bImage
        place = board[num].create_image(55, 55, image=display)

    # white
    setCounter = 0
    for num in range(63, 47, -1):
        piece = wSet[setCounter]
        board_spaces[num] = piece
        display = white_pieces[setCounter].wImage
        place = board[num].create_image(55, 55, image=display)
        setCounter += 1

    return black_pieces, white_pieces, board, board_spaces

# try to set positions based on FEN


labels_top()
blackSquares, whiteSquares = make_board()
black_pieces, white_pieces, board, board_spaces = starting_position(
    board_spaces, board, black_pieces, white_pieces)
board = position_board(blackSquares, whiteSquares)

root.mainloop()
