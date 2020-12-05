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
import fontexplorer as fe
# import houghtransform as ht

def callback(font, tm, fonttype, names):
    names.append(font.lfFaceName)
    return True

fontNames = []
hdc = win32gui.GetDC(None)
win32gui.EnumFontFamilies(hdc, None, callback, fontNames)
fontNames = sorted(fontNames)
win32gui.ReleaseDC(hdc, None)
# above code from https://stackoverflow.com/questions/51256688/python-windows-enum-installed-fonts

class MainApp(App):
    def appStarted(self):
        self.fontNames = fontNames
        self.onSplashPage = True
        self.onFontTagger = False
        self.onFontExplorer = False
        
        sp.initSPvars(self)
        ft.initFTvars(self)
        fe.initFEvars(self)

    def mousePressed(self, event):
        if self.onSplashPage:
            sp.mousePressed(self, event)
        if self.onFontTagger:
            ft.mousePressed(self, event)
        if self.onFontExplorer:
            fe.mousePressed(self, event)
        # ht.runHoughTransform(self)

    def keyPressed(self, event):
        if self.onFontTagger:
            ft.keyPressed(self, event)
        if self.onFontExplorer:
            fe.keyPressed(self, event)

    # TODO: add a clear all tags button
    # TODO: add a box for searching for a font
    def redrawAll(self, canvas):
        if self.onSplashPage:
            sp.drawSplashPageUI(self, canvas)
        if self.onFontTagger:
            ft.drawFontTaggerUI(self, canvas)
        if self.onFontExplorer:
            fe.drawFontExplorerUI(self, canvas)

MainApp(width = 500, height = 500, mvcCheck = False)