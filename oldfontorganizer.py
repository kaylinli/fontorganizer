import win32gui
from tkinter import font
import tkinter as tk
from cmu_112_graphics import *

def callback(font, tm, fonttype, names):
    names.append(font.lfFaceName)
    return True

fontNames = []
hdc = win32gui.GetDC(None)
win32gui.EnumFontFamilies(hdc, None, callback, fontNames)
# print("\n".join(fontnames))
fontNames = sorted(fontNames)
print(fontNames)
win32gui.ReleaseDC(hdc, None)
# above code from https://stackoverflow.com/questions/51256688/python-windows-enum-installed-fonts


def appStarted(app):
    
    app.startEntries = 70 # y position of where the entries start
    app.entryHeight = 20 # space between entries
    app.marginLeft = 10
    app.headerWidth = 70

    app.fontEntries = (app.width-app.headerWidth)//20 - 2# number of entries on a page
    app.pageNum = 0 # page number starts at 0
    app.totalPages = len(fontNames) // app.fontEntries

    app.tagInputX = (app.marginLeft, app.marginLeft+100)
    app.tagInputY = 55, 55+20
    app.isTypingTag = False
    app.tagInput = ""
    

    # variables for page navigation
    app.forwardButtonX = app.width/2 + 20
    app.forwardButtonY = app.height - 10
    app.backButtonX = app.width/2 - 20
    app.backButtonY = app.height - 10

def mousePressed(app, event):
    checkForNavigation(app, event)
    checkForTagInput(app, event)

# checks if navigation buttons are pressed
def checkForNavigation(app, event):
    if app.forwardButtonX-20 < event.x < app.forwardButtonX+20:
        app.pageNum += 1
    if app.backButtonX-20 < event.x < app.backButtonX+20:
        # disables back button on 0th page
        if app.pageNum != 0:
            app.pageNum -= 1
    app.pageNum = app.pageNum % app.totalPages

def checkForTagInput(app,event):
    if app.tagInputX[0] < event.x < app.tagInputX[1] and \
        app.tagInputY[0] < event.y < app.tagInputY[1]:
        app.isTypingTag = True


def keyPressed(app, event):
    if isTypingTag:
        app.tagInput += event.key 

def pageSetup(app, canvas):
    count = app.startEntries + app.entryHeight
    firstEntry = app.pageNum * app.fontEntries
    for fontFamily in fontNames[firstEntry:(firstEntry+app.fontEntries)]:
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

def createHeader(app,canvas):
    canvas.create_text(app.marginLeft, 30, text="font tagger", anchor="w", font=("Red Hat Display Medium", 24))
    
    x0,x1 = app.tagInputX[0], app.tagInputX[1]
    y0,y1 = app.tagInputY[0], app.tagInputY[1]
    canvas.create_rectangle(x0, y0, x1, y1)
    canvas.create_text(x0+5, y0+3, anchor="nw", text="type tag here")
    
def redrawAll(app, canvas):
    pageSetup(app, canvas)
    createHeader(app,canvas)
    createNavigationButtons(app,canvas)

runApp(width = 500, height = 500)