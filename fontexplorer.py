import win32gui
from tkinter import font
import tkinter as tk
from cmu_112_graphics import *

# import other files
import utility as util

'''
Model
'''

def initFEvars(app, canvas):
    pass

'''
Controller
'''
def mousePressed(app, event):
    pass

'''
View
'''

def createHeader(app, canvas):
    canvas.create_text(app.marginLeft, 30, text="font tagger", anchor="w", font=("Red Hat Display Medium", 24))
    
    drawTagInputBox(app, canvas)


def drawFontExplorerUI(app, canvas):
    pass