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
    # coordinates of header/logo thing
    app.nameCoords = app.width/2, app.height*(3/7)

    app.buttonWidth = 150
    app.buttonHeight = 30
    # font tagger button location
    app.fontTaggerBtnCoords = (app.width*(2/7), app.nameCoords[1] + 70)
    app.fontTaggerBtnX = (app.fontTaggerBtnCoords[0] - app.buttonWidth/2,
                          app.fontTaggerBtnCoords[0] + app.buttonWidth/2)
    app.fontTaggerBtnY = (app.fontTaggerBtnCoords[1] - app.buttonHeight/2,
                          app.fontTaggerBtnCoords[1] + app.buttonHeight/2)

    # font explorer button location
    app.fontExplorerBtnCoords = (app.width*(5/7), app.nameCoords[1] + 70)
    app.fontExplorerBtnX = (app.fontExplorerBtnCoords[0] - app.buttonWidth/2,
                          app.fontExplorerBtnCoords[0] + app.buttonWidth/2)
    app.fontExplorerBtnY = (app.fontExplorerBtnCoords[1] - app.buttonHeight/2,
                          app.fontExplorerBtnCoords[1] + app.buttonHeight/2)

'''
Controller
'''

def mousePressed(app, event):
    # if clicked font tagger button
    if util.checkIfClickedButton(event.x, event.y, 
                        app.fontTaggerBtnCoords[0], app.fontTaggerBtnCoords[1], 
                        app.buttonWidth, app.buttonHeight):
        app.onSplashPage = False
        app.onFontTagger = True
    # if clicked font explorer button
    if util.checkIfClickedButton(event.x, event.y, 
                    app.fontExplorerBtnCoords[0], app.fontExplorerBtnCoords[1], 
                    app.buttonWidth, app.buttonHeight):
        app.onSplashPage = False
        app.onFontExplorer = True

'''
View
'''

def createHeader(app, canvas):
    canvas.create_text(app.nameCoords[0], app.nameCoords[1], 
                        text="font organizer", font=("Red Hat Display Bold", 40))

def createFontTaggerBtn(app, canvas):
    canvas.create_rectangle(app.fontTaggerBtnX[0], app.fontTaggerBtnY[0],
                            app.fontTaggerBtnX[1], app.fontTaggerBtnY[1])
    canvas.create_text(app.fontTaggerBtnCoords[0], app.fontTaggerBtnCoords[1],
                         text="font tagger", font=("Red Hat Display", 14))

def createFontExplorerBtn(app, canvas):
    canvas.create_rectangle(app.fontExplorerBtnX[0], app.fontExplorerBtnY[0],
                            app.fontExplorerBtnX[1], app.fontExplorerBtnY[1])
    canvas.create_text(app.fontExplorerBtnCoords[0], app.fontExplorerBtnCoords[1], text="font explorer", font=("Red Hat Display", 15))

def drawSplashPageUI(app, canvas):
    createHeader(app, canvas)
    createFontTaggerBtn(app, canvas)
    createFontExplorerBtn(app, canvas)
