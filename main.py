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
import fontboard as fb
import autofonttagger as at
import fontwidget as fw
# import houghtransform as ht

def callback(font, tm, fonttype, names):
    names.append(font.lfFaceName)
    return True

fontNames = []
hdc = win32gui.GetDC(None)
win32gui.EnumFontFamilies(hdc, None, callback, fontNames)
fontNames = sorted(fontNames)
win32gui.ReleaseDC(hdc, None)
# above code taken from https://stackoverflow.com/questions/51256688/python-windows-enum-installed-fonts

class MainApp(ModalApp):
    def appStarted(app):
        app.fontNames = fontNames
        app.fontTags = dict()
        # app.onSplashPage = True
        # app.onFontTagger = False
        # app.onFontExplorer = False
        
        app.splashPage = sp.SplashPage()
        app.fontTagger = ft.FontTagger()
        app.fontBoard = fb.FontBoard()
        app.autoFontTagger = at.AutoFontTagger() 
        app.fontWidget = fw.FontWidget()

        app.initializeFontTags()

        app.setActiveMode(app.splashPage)

    def initializeFontTags(app):
        print("reading")
        file = open("fonttags.txt", "r")
        # data = file.read()
        for line in file:
            # line = file.readline()
            # example line: "Arial: Sans serif, project1"
            colonIndex = line.find(":")
            font = line[:colonIndex]
            tags = line[colonIndex+2:].split(", ") # colonIndex+2 because of ": "
            for tag in tags:
                # print("tag.strip()",repr(tag.strip()))
                if font not in app.fontTags:
                    app.fontTags[font] = [tag.strip()]
                else:
                    app.fontTags[font] += [tag.strip()]
        
    #     sp.initSPvars(self)
    #     ft.initFTvars(self)
    #     fe.initFEvars(self)
    
    # def appStopped(self):
    #     ft.appStopped(self)

    # def mousePressed(self, event):
    #     if self.onSplashPage:
    #         sp.mousePressed(self, event)
    #     if self.onFontTagger:
    #         ft.mousePressed(self, event)
    #     if self.onFontExplorer:
    #         fe.mousePressed(self, event)
    #     # ht.runHoughTransform(self)

    # def keyPressed(self, event):
    #     if self.onFontTagger:
    #         ft.keyPressed(self, event)
    #     if self.onFontExplorer:
    #         fe.keyPressed(self, event)

    # # TODO: add a clear all tags button
    # # TODO: add a box for searching for a font
    # def redrawAll(self, canvas):
    #     if self.onSplashPage:
    #         sp.drawSplashPageUI(self, canvas)
    #     if self.onFontTagger:
    #         ft.drawFontTaggerUI(self, canvas)
    #     if self.onFontExplorer:
    #         fe.drawFontExplorerUI(self, canvas)

app = MainApp(width = 500, height = 500, mvcCheck = False)