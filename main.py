'''
This code is written by Kaylin Li. 
All code not written by Kaylin is credited next to the corresponding section.
'''

import win32gui
from tkinter import font
import tkinter as tk
from cmu_112_graphics import *

# import other files
import splashpage as sp
import fonttagger as ft

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
    app.fontNames = fontNames
    app.onSplashPage = True
    app.onFontTagger = False
    
    sp.initSPvars(app)
    ft.initFTvars(app)

def mousePressed(app, event):
    if app.onFontTagger:
        ft.mousePressed(app, event)

def keyPressed(app, event):
    if app.onFontTagger:
        ft.keyPressed(app, event)

# TODO: add a clear all tags button
# TODO: add a box for searching for a font
def redrawAll(app, canvas):
    if app.onSplashPage:
        sp.drawSplashPageUI(app, canvas)
    if app.onFontTagger:
        ft.drawFontTaggerUI(app, canvas)

runApp(width = 500, height = 500)