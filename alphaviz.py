from typing import cast
import constantss
import validateFEN
import tkinter as tk
from PIL import Image, ImageTk
import re
from tkinter import *
from functools import partial

DEBUG = True
CORN = False


class ChessGui(tk.Frame):
    # GUI display variables
    selected = None  # selected square
    selected_piece = None
    highlighted = None

    # Initializes the AlphaViz GUI
    # Sets many instance variables, loads images used for the GUI, creates
    # most GUI components, and prepares the GUI for human interaction.
    def __init__(self, parent):
        if DEBUG:
            print("DEBUG MODE: ON")
            print("ChessGui.__init__() executing...")
        # Set parent GUI element (most likely root)
        self.parent = parent

        # Initialize tk.Frame of root
        tk.Frame.__init__(self, parent)

        # Initialize Game State Variables
        self.reset_board_state()

        # Load the images used
        self.load_images()

        # Get the width and height of the chessboard to define the initial
        # size of the canvas
        canvas_width = self.IMG_CHESSBOARD.width()
        canvas_height = self.IMG_CHESSBOARD.height()

        # Create the canvas component
        self.canvas = tk.Canvas(self, width=canvas_width,
                                height=canvas_height, background="white")
        self.canvas.pack(side="top", fill="both", anchor="c", expand=True)

        # Draw the chessboard on the canvas
        self.draw_board()

        # Directs configuration event of the canvas to call self.refresh()
        self.canvas.bind("<Configure>", self.refresh)
        # Directs left mouse click event to call self.click()
        self.canvas.bind("<Button-1>", self.click)

        # Create GUI frame at the bottom of the root frame,
        # below the chessboard canvas
        self.statusbar = tk.Frame(self, height=64)

        # Create new game button and link it to the function self.reset()
        self.button_new = tk.Button(
            self.statusbar, text="NEW", fg="black", command=self.reset)
        self.button_new.pack(side=tk.LEFT, in_=self.statusbar)

        # Create save game button and link it to the function [NONE] currently...
        self.button_save = tk.Button(
            self.statusbar, text="CLEAR", fg="black", command=self.clear_board)
        self.button_save.pack(side=tk.LEFT, in_=self.statusbar)

        # [TEMPORARY DEMO FEATURE]
        self.button_immortal = tk.Button(
            self.statusbar, text='IMMORTAL', fg="black", command=self.immortal)
        self.button_immortal.pack(side=tk.LEFT, in_=self.statusbar)

        # Create the quit button and link it to self.parent.destroy() function
        self.button_quit = tk.Button(
            self.statusbar, text="Quit", fg="black", command=self.exit)
        self.button_quit.pack(side=tk.RIGHT, in_=self.statusbar)
        self.statusbar.pack(expand=False, fill="x", side='bottom')

        # Creates the input box for a FEN string using Entry
        self.fen_string = tk.Entry(self.statusbar)
        self.fen_string.pack(side=tk.LEFT, in_=self.statusbar)
        # uses partial from functools to help call load_fen with arguments from the button
        input_fen_string = partial(self.load_fen, self.fen_string.get())

        # Creates the load fen button and link to the load_fen(fen_string) function
        self.button_fen = tk.Button(text='Load Fen String',
                                    command=input_fen_string)
        self.button_fen.pack(side=tk.LEFT, in_=self.statusbar)
        self.statusbar.pack(expand=False, fill="x", side='bottom')

     # Display black/white's turn
        self.label_status = tk.Label(self.statusbar,
                                     text="   White to move  " if self.whitetomove else "   Black to move  ",
                                     fg="black")
        self.label_status.pack(side=tk.LEFT, expand=0, in_=self.statusbar)

    def load_images(self):
        self.IMG_CHESSBOARD = ImageTk.PhotoImage(
            file=constantss.PATH_CHESSBOARD)
        self.IMG_LTKING = ImageTk.PhotoImage(file=constantss.PATH_LTKING)
        self.IMG_DKKING = ImageTk.PhotoImage(file=constantss.PATH_DKKING)
        self.IMG_LTQUEEN = ImageTk.PhotoImage(file=constantss.PATH_LTQUEEN)
        self.IMG_DKQUEEN = ImageTk.PhotoImage(file=constantss.PATH_DKQUEEN)
        self.IMG_LTROOK = ImageTk.PhotoImage(file=constantss.PATH_LTROOK)
        self.IMG_DKROOK = ImageTk.PhotoImage(file=constantss.PATH_DKROOK)
        self.IMG_LTBISHOP = ImageTk.PhotoImage(file=constantss.PATH_LTBISHOP)
        self.IMG_DKBISHOP = ImageTk.PhotoImage(file=constantss.PATH_DKBISHOP)
        self.IMG_LTKNIGHT = ImageTk.PhotoImage(
            file=constantss.PATH_LTUNICORN if CORN else constantss.PATH_LTKNIGHT)
        self.IMG_DKKNIGHT = ImageTk.PhotoImage(
            file=constantss.PATH_DKUNICORN if CORN else constantss.PATH_DKKNIGHT)
        self.IMG_LTPAWN = ImageTk.PhotoImage(file=constantss.PATH_LTPAWN)
        self.IMG_DKPAWN = ImageTk.PhotoImage(file=constantss.PATH_DKPAWN)

    def load_fen(self, fen_string):
        if DEBUG:
            print(f'ChessGui.load_fen(\'{fen_string}\') executing...')

        self.reset_board_state()

        if validateFEN.fenPass(fen_string):
            if DEBUG:
                print(f'\'{fen_string}\' is a valid FEN string!')

            # Tokenize
            tokens = fen_string.split(' ')
            board_str = tokens[0]
            bwturn_str = tokens[1]
            castles_str = tokens[2]
            enpassant_str = tokens[3]
            halfmoves_str = tokens[4]
            moves_str = tokens[5]

            # set self.whitetomove
            if bwturn_str == 'w':
                self.whitetomove = True
            else:
                self.whitetomove = False

            # set en passant move
            self.possible_enpassant = enpassant_str
            # set the half moves and moves
            self.half_moves = int(halfmoves_str)
            self.moves = int(moves_str)

            # parse castling
            if 'K' in castles_str:
                self.wk_castle = True
            if 'Q' in castles_str:
                self.wq_castle = True
            if 'k' in castles_str:
                self.bk_castle = True
            if 'q' in castles_str:
                self.bq_castle = True

            # parse board
            # DO NOT TWEAK THESE NUMBERS THEY WERE CAREFULLY MANUFACTURED
            i = 56
            for character in board_str:
                if character == '/':
                    i -= 16
                elif character.isdigit():
                    i += int(character)
                elif character == 'P':
                    self.board[i] = constantss.LTPAWN
                    i += 1
                elif character == 'p':
                    self.board[i] = constantss.DKPAWN
                    i += 1
                elif character == 'R':
                    self.board[i] = constantss.LTROOK
                    i += 1
                elif character == 'r':
                    self.board[i] = constantss.DKROOK
                    i += 1
                elif character == 'K':
                    self.board[i] = constantss.LTKING
                    i += 1
                elif character == 'k':
                    self.board[i] = constantss.DKKING
                    i += 1
                elif character == 'B':
                    self.board[i] = constantss.LTBISHOP
                    i += 1
                elif character == 'b':
                    self.board[i] = constantss.DKBISHOP
                    i += 1
                elif character == 'Q':
                    self.board[i] = constantss.LTQUEEN
                    i += 1
                elif character == 'q':
                    self.board[i] = constantss.DKQUEEN
                    i += 1
                elif character == 'N':
                    self.board[i] = constantss.LTKNIGHT
                    i += 1
                elif character == 'n':
                    self.board[i] = constantss.DKKNIGHT
                    i += 1
        else:
            if DEBUG:
                print(f'{fen_string} is NOT a valid FEN string!')
                print('[ERROR] load_fen() Failed.')

    def board_to_fen(self):
        if DEBUG:
            print('ChessGui.board_to_fen() executing...')

    def click(self, event):
        if DEBUG:
            print('ChessGui.click() executing...')

    def move(self, p1, p2):
        if DEBUG:
            print('ChessGui.move() executing...')

    def highlight(self, pos):
        if DEBUG:
            print('ChessGui.highlight() executing...')

    def addpiece(self, name, image, row=0, column=0):
        if DEBUG:
            print('ChessGui.addpiece() executing...')

    def placepiece(self, name, row, column):
        if DEBUG:
            print('ChessGui.placepiece() executing...')

    def refresh(self, event={}):
        # NEED TO IMPLEMENT!!
        if DEBUG:
            print('ChessGui.refresh() executing...')

    def draw_pieces(self):
        if DEBUG:
            print('ChessGui.draw_pieces() executing...')
        # Starting pixel counts for A1-square
        x_pos = constantss.BOARD_OFFSET  # = 30
        y_pos = constantss.BOARD_SIZE - constantss.BOARD_OFFSET - constantss.SQUARE_SIZE
        # = 590

        for rank in range(0, 8):
            for file in range(0, 8):
                ind = rank*8 + file

                # The ordering of these if statements were created in the wee hours
                # of the night by Zander. The logic is strange but they matter
                # for efficiency. If you are unconvinced, that is okay.
                # The gist of it is that we check the most likely pieces first

                if self.board[ind] == constantss.EMPTY:
                    # Don't draw anything if the square is empty
                    pass
                elif self.board[ind] == constantss.LTPAWN:
                    self.canvas.create_image(
                        x_pos, y_pos, anchor='nw', image=self.IMG_LTPAWN)
                elif self.board[ind] == constantss.DKPAWN:
                    self.canvas.create_image(
                        x_pos, y_pos, anchor='nw', image=self.IMG_DKPAWN)
                elif self.board[ind] == constantss.LTROOK:
                    self.canvas.create_image(
                        x_pos, y_pos, anchor='nw', image=self.IMG_LTROOK)
                elif self.board[ind] == constantss.DKROOK:
                    self.canvas.create_image(
                        x_pos, y_pos, anchor='nw', image=self.IMG_DKROOK)
                elif self.board[ind] == constantss.LTKING:
                    self.canvas.create_image(
                        x_pos, y_pos, anchor='nw', image=self.IMG_LTKING)
                elif self.board[ind] == constantss.DKKING:
                    self.canvas.create_image(
                        x_pos, y_pos, anchor='nw', image=self.IMG_DKKING)
                elif self.board[ind] == constantss.LTBISHOP:
                    self.canvas.create_image(
                        x_pos, y_pos, anchor='nw', image=self.IMG_LTBISHOP)
                elif self.board[ind] == constantss.DKBISHOP:
                    self.canvas.create_image(
                        x_pos, y_pos, anchor='nw', image=self.IMG_DKBISHOP)
                elif self.board[ind] == constantss.LTQUEEN:
                    self.canvas.create_image(
                        x_pos, y_pos, anchor='nw', image=self.IMG_LTQUEEN)
                elif self.board[ind] == constantss.DKQUEEN:
                    self.canvas.create_image(
                        x_pos, y_pos, anchor='nw', image=self.IMG_DKQUEEN)
                elif self.board[ind] == constantss.LTKNIGHT:
                    self.canvas.create_image(
                        x_pos, y_pos, anchor='nw', image=self.IMG_LTKNIGHT)
                elif self.board[ind] == constantss.DKKNIGHT:
                    self.canvas.create_image(
                        x_pos, y_pos, anchor='nw', image=self.IMG_DKKNIGHT)
                else:
                    print(
                        "[ERROR] ChessGui.draw_pieces(): board[ind] value matches no piece!")

                x_pos += constantss.SQUARE_SIZE
            # End inner for loop
            x_pos = constantss.BOARD_OFFSET
            y_pos -= 80
        # End outer for loop
    # End draw_pieces()

    def draw_board(self):
        if DEBUG:
            print('ChessGui.draw_board() executing...')
        self.canvas.create_image(0, 0, anchor='nw', image=self.IMG_CHESSBOARD)

    def reset_board_state(self):
        # initialize empty board. index 0 is A1 and 63 is H8
        self.board = [0]*64
        self.whitetomove = True
        self.wk_castle = True           # Not yet implemented in load_fen()
        self.wq_castle = True           # Not yet implemented in load_fen()
        self.bk_castle = True           # Not yet implemented in load_fen()
        self.bq_castle = True           # Not yet implemented in load_fen()
        self.possible_enpassant = '-'   # Not yet implemented in load_fen()
        self.half_moves = 0             # Not yet implemented in load_fen()
        self.full_moves = 1             # Not yet implemented in load_fen()

    def immortal(self):
        if DEBUG:
            print('ChessGui.immortal() executing...')
        self.canvas.delete('all')
        self.draw_board()
        self.load_fen(constantss.FEN_IMMORTAL_GAME)
        self.draw_pieces()

    def clear_board(self):
        if DEBUG:
            print('ChessGui.clear_board() executing...')

        self.canvas.delete('all')
        self.draw_board()
        self.load_fen(constantss.FEN_EMPTY)
        self.draw_pieces()

    def reset(self):
        if DEBUG:
            print('ChessGui.reset() executing...')

        # Reset board state
        self.canvas.delete('all')
        self.draw_board()
        self.load_fen(constantss.FEN_STARTING_POSITION)
        self.draw_pieces()

    def exit(self):
        if DEBUG:
            print("ChessGui.exit() executing...")
        self.parent.destroy()


def display():
    root = tk.Tk()
    root.title('AlphaViz')
    root.resizable(width=False, height=False)

    gui = ChessGui(root)
    gui.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.mainloop()
    if DEBUG:
        print('display() completed gracefully')


if __name__ == "__main__":
    display()
    if DEBUG:
        print('chess_gui main completed gracefully')
