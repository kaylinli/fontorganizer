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

def initFTvars(app):
    # layout stuff
    app.headerWidth = 70
    app.startEntries = 70 # y position of where the entries start
    app.entryHeight = 20 # space between entries
    app.marginLeft = 10

    # page stuff
    app.fontEntries = (app.height-app.headerWidth)//20 - 2# number of entries on a page
    app.pageNum = 0 # page number starts at 0
    app.totalPages = len(app.fontNames) // app.fontEntries

    # tag input variables
    app.tagInputX = (app.marginLeft, app.marginLeft+100)
    app.tagInputY = 55, 55+20
    app.isTypingTag = False
    app.tagInput = ""
    
    # variables for page navigation
    app.forwardButtonX = app.width/2 + 20
    app.forwardButtonY = app.height - 10
    app.backButtonX = app.width/2 - 20
    app.backButtonY = app.height - 10

'''
Controller
'''

def mousePressed(app, event):
    checkForNavigation(app, event)
    checkForTagInput(app, event)

# checks if navigation buttons are pressed
def checkForNavigation(app, event):
    if util.checkIfClickedButton(event.x, event.y, 
                app.forwardButtonX-20, app.forwardButtonY-20, 
                app.forwardButtonX+20, app.forwardButtonY+20):
        app.pageNum += 1
    if util.checkIfClickedButton(event.x, event.y, 
                app.backButtonX-20, app.backButtonY-20, 
                app.backButtonX+20, app.backButtonY+20):
        # if app.pageNum != 0: disables back button on 0th page
        app.pageNum -= 1
    app.pageNum = app.pageNum % app.totalPages

def checkForTagInput(app,event):
    if util.checkIfClickedButton(event.x, event.y, 
                            app.tagInputX[0], app.tagInputY[0], 
                            app.tagInputX[1], app.tagInputY[1]):
        app.isTypingTag = True
        app.isTypingTag = True
    else:
        app.isTypingTag = False
    # TODO: check if 'x' button was clicked to clear tag input


def keyPressed(app, event):
    if app.isTypingTag:
        app.tagInput += event.key 

'''
View
'''

def pageSetup(app, canvas):
    count = app.startEntries + app.entryHeight
    firstEntry = app.pageNum * app.fontEntries
    for fontFamily in app.fontNames[firstEntry:(firstEntry+app.fontEntries)]:
        try:
            fontType = font.Font(family=fontFamily,size=14)
            canvas.create_text(app.marginLeft, count, anchor='w', text=f'{fontFamily}', font=fontType)
        except Exception as e:
            print(e)
            print(fontFamily)
        count += app.entryHeight

def createNavigationButtons(app,canvas):
    # TODO: add buttons to jump to a page, or have  |<| |1| |2| ... |20| |>| 
    # inspo: https://cdn2.vectorstock.com/i/1000x1000/47/91/pagination-bar-page-navigation-web-buttons-vector-22654791.jpg
    # inspo2: https://cdn4.vectorstock.com/i/1000x1000/47/88/pagination-bar-page-navigation-web-buttons-vector-22654788.jpg
    canvas.create_rectangle(app.forwardButtonX-10, app.forwardButtonY-10, app.forwardButtonX+10,app.forwardButtonY+10)
    canvas.create_rectangle(app.backButtonX-10, app.backButtonY-10, app.backButtonX+10,app.backButtonY+10)
    canvas.create_text(app.forwardButtonX, app.forwardButtonY, text='>')
    canvas.create_text(app.backButtonX, app.backButtonY, text='<')

def createHeader(app, canvas):
    canvas.create_text(app.marginLeft, 30, text="font tagger", anchor="w", font=("Red Hat Display Medium", 24))
    
    drawTagInputBox(app, canvas)

def drawTagInputBox(app, canvas):
    # create box
    x0, x1 = app.tagInputX[0], app.tagInputX[1]
    y0, y1 = app.tagInputY[0], app.tagInputY[1]
    canvas.create_rectangle(x0, y0, x1, y1)

    # create text inside box
    # TODO: make text wrap around if it goes outside box'
    if app.tagInput == "" and app.isTypingTag == False:
        canvas.create_text(x0+5, y0+3, anchor="nw", text="type tag here")
    else: # if app.isTypingTag == True
        canvas.create_text(x0+5, y0+3, anchor="nw", text=f"{app.tagInput}")

    # create clear button
    x0, x1 = app.tagInputX[1]+10, app.tagInputX[1]+30
    y0, y1 = app.tagInputY[0], app.tagInputY[0]+20
    canvas.create_rectangle(x0, y0, x1, y1)
    canvas.create_text(x0+10, y0+10, anchor="center", text="×", font=("Red Hat Display", 14))

def drawFontTaggerUI(app, canvas):
    pageSetup(app, canvas)
    createHeader(app,canvas)
    createNavigationButtons(app,canvas)

'''
Generic Utility Functions
'''

