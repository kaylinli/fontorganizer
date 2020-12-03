import win32gui
from tkinter import font
import tkinter as tk
from cmu_112_graphics import *

# import other files
import utility as util

'''
Model
'''

def initFEvars(self, canvas):
    pass

'''
Controller
'''
def mousePressed(self, event):
    pass

'''
View
'''

def createHeader(self, canvas):
    canvas.create_text(self.marginLeft, 30, text="font tagger", anchor="w", font=("Red Hat Display Medium", 24))
    
    drawTagInputBox(self, canvas)


def drawFontExplorerUI(self, canvas):
    pass