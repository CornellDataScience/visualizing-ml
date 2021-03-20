import tkinter as tk
from PIL import Image, ImageTk

FEN_STARTING_POSITION = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
FEN_1E4 = 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1'

class ChessGui(tk.Frame):
    pieces = {}
    selected = None
    selected_piece = None
    highlighted = None
    icons = {}

    rows = 8
    columns = 8

    @property
    def canvas_size(self):
        return (self.columns * self.square_size, self.rows * self.square_size)

    def __init__(self, parent, chessboard, square_size=64):
        pass

    def click(self, event):
        pass

    def move(self, p1, p2):
        pass

    def highlight(self, pos):
        pass

    def addpiece(self, name, image, row=0, column=0):
        pass

    def placepiece(self, name, row, column):
        pass

    def refresh(self, event={}):
        pass

    def draw_pieces(self):
        pass

    def reset(self):
        pass
        

def display():
    root = tk.Tk()
    root.title('Visualizing ML Chess Gui')

    gui = ChessGui(root)
    gui.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.mainloop()
    print('hello world');

if __name__ == "__main__":
    display()