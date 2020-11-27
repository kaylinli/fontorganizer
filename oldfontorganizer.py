'''
import os
from cmu_112_graphics import *

list = []
for file in os.listdir(r'C:\Windows\Fonts'):
    if file.endswith(".ttf"):
        list.append(file)
    if file.endswith(".otf"):
        list.append(file)

# above is code by Bhavesh Mevada, modified slightly
# https://stackoverflow.com/questions/54832003/how-to-retrieve-actual-font-file-name-in-python
'''

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
    

    # variables for page navigation
    app.forwardButtonX = app.width/2 + 20
    app.forwardButtonY = app.height - 10
    app.backButtonX = app.width/2 - 20
    app.backButtonY = app.height - 10

def mousePressed(app, event):
    if app.forwardButtonX-20 < event.x < app.forwardButtonX+20:
        app.pageNum += 1
    if app.backButtonX-20 < event.x < app.backButtonX+20:
        # disables back button on 0th page
        if app.pageNum != 0:
            app.pageNum -= 1
    app.pageNum = app.pageNum % app.totalPages

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
    inputwidth = 100
    inputheight = 20
    x0,x1 = app.marginLeft, app.marginLeft+inputwidth
    y0,y1 = 55, 55+inputheight
    canvas.create_rectangle(x0, y0, x1, y1)
    canvas.create_text(x0+5, y0+3, anchor="nw", text="type tag here")
    
def redrawAll(app, canvas):
    pageSetup(app, canvas)
    createHeader(app,canvas)
    createNavigationButtons(app,canvas)

runApp(width = 500, height = 500)