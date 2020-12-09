'''
File: board.py
Author: Kaylin Li
Purpose: displays saved images of fonts as a "board"
All code not written by Kaylin is credited next to the corresponding section.
'''
import win32gui
from tkinter import font
import tkinter as tk
from cmu_112_graphics import *

import os
import random

# import other files
import utility as util

class Board(Mode):
    # file io structure taken from https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html
    def redrawAll(self, canvas):
        for file in os.listdir("fontboard"):
            if file != None:
                print("file", file)
                try:
                    # self.image = self.loadImage(f"fontboard/{file}")
                    self.image = self.loadImage("n.png")
                    canvas.create_image(200, 300, image=ImageTk.PhotoImage(self.image))
                except:
                    print("We're having trouble recognizing your image")
                