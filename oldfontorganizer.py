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
    # y position of where the startEntries
    app.startEntries = 50
    # space between entries
    app.entryHeight = 20
    app.fontEntries = app.width//20 - 2# number of entries on a page
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
            canvas.create_text(10, count, anchor='w', text=f'{fontFamily}', font=fontType)
        except Exception as e:
            print(e)
            print(fontFamily)
        count += app.entryHeight

def createNavigationButtons(app,canvas):
    canvas.create_rectangle(app.forwardButtonX-10, app.forwardButtonY-10, app.forwardButtonX+10,app.forwardButtonY+10)
    canvas.create_rectangle(app.backButtonX-10, app.backButtonY-10, app.backButtonX+10,app.backButtonY+10)
    canvas.create_text(app.forwardButtonX, app.forwardButtonY, text='>')
    canvas.create_text(app.backButtonX, app.backButtonY, text='<')

def createHeader(app,canvas):
    canvas.create_text(app.width/2, 20, text="Font organizer", font=("Red Hat Display", 24))
    
def redrawAll(app, canvas):
    pageSetup(app, canvas)
    createNavigationButtons(app,canvas)

runApp(width = 500, height = 500)