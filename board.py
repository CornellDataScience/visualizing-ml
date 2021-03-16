import tkinter as tk
from PIL import ImageTk, ImageTk
import random

#base window
root = tk.Tk()
root.title("Visualizing ML")
root.geometry("1000x1000")

#header
header = tk.Label(root, text = "Chess Board")
header.grid(column=0, row=0)

def board_top():
  top_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
  count = 1
  for label in top_letters:
    label = tk.Label(root, text=label)
    label.grid(column=count, row=0)
    count+=1
board_top()
root.mainloop()