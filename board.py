import tkinter as tk
from PIL import ImageTk, ImageTk
import random

#base window
root = tk.Tk()
root.title("Visualizing ML")
root.geometry("1000x1000")

global blackSquares
global whiteSquares
#labels
def labels_top():
  top_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
  count = 1
  for label in top_letters:
    label = tk.Label(root, text=label)
    label.grid(column=count, row=0)
    count+=1

def make_board():
  blackSquares = []
  blackSquares+=range(0,32)

  whiteSquares = []
  whiteSquares+=range(0,32)

  for var in blackSquares:
    ind = blackSquares.index(var)
    blackSquares[ind] = tk.Canvas(root, width=80,height=80,border=0,bg="blue4",cursor="hand2")
            
  for var in whiteSquares:
    ind = whiteSquares.index(var)
    whiteSquares[ind] = tk.Canvas(root, width=80,height=80,border=0,bg="navajo white",cursor="hand2")
            
  return blackSquares,whiteSquares

def position_board(blackSquares,whiteSquares):
        bCol = 0
        wCol = -1
        for num in range(0,4):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=1)
            whiteSquares[num].grid(column=wCol,row=1)

        bCol = -1
        wCol = 0
        for num in range(4,8):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=2)
            whiteSquares[num].grid(column=wCol,row=2)

        bCol = 0
        wCol = -1
        for num in range(8,12):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=3)
            whiteSquares[num].grid(column=wCol,row=3)

        bCol = -1
        wCol = 0
        for num in range(12,16):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=4)
            whiteSquares[num].grid(column=wCol,row=4)

        bCol = 0
        wCol = -1
        for num in range(16,20):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=5)
            whiteSquares[num].grid(column=wCol,row=5)

        bCol = -1
        wCol = 0
        for num in range(20,24):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=6)
            whiteSquares[num].grid(column=wCol,row=6)

        bCol = 0
        wCol = -1
        for num in range(24,28):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=7)
            whiteSquares[num].grid(column=wCol,row=7)

        bCol = -1
        wCol = 0
        for num in range(28,32):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=8)
            whiteSquares[num].grid(column=wCol,row=8)

        board = []
        for num in range(0,4):
                board.append(whiteSquares[num])
                board.append(blackSquares[num])
        for num in range(4,8):
                board.append(blackSquares[num])
                board.append(whiteSquares[num])
        for num in range(8,12):
                board.append(whiteSquares[num])
                board.append(blackSquares[num])
        for num in range(12,16):
                board.append(blackSquares[num])
                board.append(whiteSquares[num])
        for num in range(16,20):
                board.append(whiteSquares[num])
                board.append(blackSquares[num])
        for num in range(20,24):
                board.append(blackSquares[num])
                board.append(whiteSquares[num])
        for num in range(24,28):
                board.append(whiteSquares[num])
                board.append(blackSquares[num])
        for num in range(28,32):
                board.append(blackSquares[num])
                board.append(whiteSquares[num])
        return board

labels_top()
blackSquares,whiteSquares = make_board()
board = position_board(blackSquares,whiteSquares)
root.mainloop()