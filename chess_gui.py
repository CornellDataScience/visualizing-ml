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

    def __init__(self, parent):
        # Set parent GUI element (most likely root)
        self.parent = parent

        # Initialize tk.Frame of root
        tk.Frame.__init__(self, parent)

        # Load the chessboard and chess pieces pngs
        self.IMG_CHESSBOARD = ImageTk.PhotoImage(file=r'imgs/chessboard_nbkgd.png')
        self.IMG_LTKING = ImageTk.PhotoImage(file=r'imgs/king_light.png')
        self.IMG_DKKING = ImageTk.PhotoImage(file=r'imgs/king_dark.png')
        self.IMG_LTQUEEN = ImageTk.PhotoImage(file=r'imgs/queen_light.png')
        self.IMG_DKQUEEN = ImageTk.PhotoImage(file=r'imgs/queen_dark.png')
        self.IMG_LTROOK = ImageTk.PhotoImage(file=r'imgs/rook_light.png')
        self.IMG_DKROOK = ImageTk.PhotoImage(file=r'imgs/rook_dark.png')
        self.IMG_LTBISHOP = ImageTk.PhotoImage(file=r'imgs/bishop_light.png')
        self.IMG_DKBISHOP = ImageTk.PhotoImage(file=r'imgs/bishop_dark.png')
        self.IMG_LTKNIGHT = ImageTk.PhotoImage(file=r'imgs/knight_light.png')
        self.IMG_DKKNIGHT = ImageTk.PhotoImage(file=r'imgs/knight_dark.png')
        self.IMG_LTPAWN = ImageTk.PhotoImage(file=r'imgs/pawn_light.png')
        self.IMG_DKPAWN = ImageTk.PhotoImage(file=r'imgs/pawn_dark.png')
        self.IMG_LTUNICORN = ImageTk.PhotoImage(file=r'imgs/unicorn_light.png')
        self.IMG_DKUNICORN = ImageTk.PhotoImage(file=r'imgs/unicorn_dark.png')

        # Get the width and height of the chessboard to define the initial 
        # size of the canvas
        canvas_width = self.IMG_CHESSBOARD.width()
        canvas_height = self.IMG_CHESSBOARD.height()

        # Create the canvas
        self.canvas = tk.Canvas(self, width=canvas_width, height=canvas_height, background="white")
        self.canvas.pack(side="top", fill="both", anchor="c", expand=True)

        # Draw the chessboard
        self.canvas.create_image(0,0,anchor='nw',image=self.IMG_CHESSBOARD)
        # Draw the test unicorn images
        self.canvas.create_image(30,30,anchor='nw',image=self.IMG_DKUNICORN)
        self.canvas.create_image(30,590,anchor='nw',image=self.IMG_LTUNICORN)

        # Not entire sure what these two lines do yet...
        self.canvas.bind("<Configure>", self.refresh)
        self.canvas.bind("<Button-1>", self.click)

        # Create GUI region at the bottom of the root frame
        self.statusbar = tk.Frame(self, height=64)

        # Create new game button and link it to the function self.reset()
        self.button_new = tk.Button(self.statusbar, text="New", fg="black", command=self.reset)
        self.button_new.pack(side=tk.LEFT, in_=self.statusbar)

        # Create save game button and link it to the function [NONE] currently...
        self.button_save = tk.Button(self.statusbar, text="Save", fg="black", command=None)
        self.button_save.pack(side=tk.LEFT, in_=self.statusbar)

        # Display black/white's turn
        self.label_status = tk.Label(self.statusbar, text="   White to move  ", fg="black")
        self.label_status.pack(side=tk.LEFT, expand=0, in_=self.statusbar)

        # Create the quit button and link it to self.parent.destroy() function
        self.button_quit = tk.Button(self.statusbar, text="Quit", fg="black", command=self.parent.destroy)
        self.button_quit.pack(side=tk.RIGHT, in_=self.statusbar)
        self.statusbar.pack(expand=False, fill="x", side='bottom')


    def load_fen(self, fen_string):
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
        print('draw_pieces() finished');
        pass

    def reset(self):
        pass
        

def display():
    root = tk.Tk()
    root.title('AlphaViz')
    root.resizable(width=False, height=False)

    gui = ChessGui(root)
    gui.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    gui.draw_pieces()
    root.mainloop()
    print('display() finished');

if __name__ == "__main__":
    display()
    print('chess_gui main finished')