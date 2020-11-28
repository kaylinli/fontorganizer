'''
This code is written by Kaylin Li. 
All code not written by Kaylin is credited next to the corresponding section.
'''

import win32gui
from tkinter import font
import tkinter as tk
from cmu_112_graphics import *

# import other files
import utility as util

'''
Model
'''
def initSPvars(app):

    app.nameCoords = app.width/2, app.height*(3/7)

    app.buttonWidth = 150
    app.buttonHeight = 30
    app.fontTaggerBtnCoords = (app.width*(2/7), app.nameCoords[1] + 70)
    app.fontExplorerBtnCoords = (app.width*(5/7), app.nameCoords[1] + 70)

'''
Controller
'''

def mousePressed(app):
    pass

'''
View
'''

def createHeader(app, canvas):
    canvas.create_text(app.nameCoords[0], app.nameCoords[1], 
                        text="font organizer", font=("Red Hat Display Bold", 40))

def createFontTaggerBtn(app, canvas):
    x0 = app.fontTaggerBtnCoords[0] - app.buttonWidth/2
    y0 = app.fontTaggerBtnCoords[1] - app.buttonHeight/2
    x1 = x0 + app.buttonWidth
    y1 = y0 + app.buttonHeight
    canvas.create_rectangle(x0, y0, x1, y1)
    canvas.create_text(app.fontTaggerBtnCoords[0], app.fontTaggerBtnCoords[1],
                         text="font tagger", font=("Red Hat Display", 14))

def createFontExplorerBtn(app, canvas):
    x0 = app.fontExplorerBtnCoords[0] - app.buttonWidth/2
    y0 = app.fontExplorerBtnCoords[1] - app.buttonHeight/2
    x1 = x0 + app.buttonWidth
    y1 = y0 + app.buttonHeight
    canvas.create_rectangle(x0, y0, x1, y1)
    canvas.create_text(app.fontExplorerBtnCoords[0], app.fontExplorerBtnCoords[1], text="font explorer", font=("Red Hat Display", 15))

def drawSplashPageUI(app, canvas):
    createHeader(app, canvas)
    createFontTaggerBtn(app, canvas)
    createFontExplorerBtn(app, canvas)
