# from tkinter import *
import tkinter as tk
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PIL import Image, ImageTk

FEN_STARTING_POSITION = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
FEN_1E4 = 'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1'

def get_svg(svg_file):
    drawing = svg2rlg(svg_file)
    renderPM.drawToFile(drawing, "temp.png", fmt="PNG")
 
class Root:
    def __init__(self):
        root = tk.Tk()
        root.title('Visualizing Machine Learning DEMO')
        root.resizable(width=False, height=False)

        img = Image.open('temp.png')
        pimg = ImageTk.PhotoImage(img)
        size = img.size
        frame = tk.Canvas(root, width=size[0], height=size[1])
        frame.pack()
        frame.create_image(0,0,anchor='nw',image=pimg)

        root.mainloop()

get_svg('svgs/chessboard.svg')
root = Root()
