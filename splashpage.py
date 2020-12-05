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

class SplashPage(Mode):
    '''
    Model
    '''
    def appStarted(self):
    # def initSPvars(self):
        # coordinates of header/logo thing
        self.nameCoords = self.width/2, self.height*(3/7)

        self.buttonWidth = 150
        self.buttonHeight = 30
        # font tagger button location
        self.fontTaggerBtnCoords = (self.width*(2/7), self.nameCoords[1] + 70)
        self.fontTaggerBtnX = (self.fontTaggerBtnCoords[0] - self.buttonWidth/2,
                            self.fontTaggerBtnCoords[0] + self.buttonWidth/2)
        self.fontTaggerBtnY = (self.fontTaggerBtnCoords[1] - self.buttonHeight/2,
                            self.fontTaggerBtnCoords[1] + self.buttonHeight/2)

        # font explorer button location
        self.fontExplorerBtnCoords = (self.width*(5/7), self.nameCoords[1] + 70)
        self.fontExplorerBtnX = (self.fontExplorerBtnCoords[0] - self.buttonWidth/2,
                            self.fontExplorerBtnCoords[0] + self.buttonWidth/2)
        self.fontExplorerBtnY = (self.fontExplorerBtnCoords[1] - self.buttonHeight/2,
                            self.fontExplorerBtnCoords[1] + self.buttonHeight/2)

    '''
    Controller
    '''

    def mousePressed(self, event):
        # if clicked font tagger button
        if util.checkIfClickedButton(event.x, event.y, 
                            self.fontTaggerBtnCoords[0], self.fontTaggerBtnCoords[1], 
                            self.buttonWidth, self.buttonHeight):
            # self.onSplashPage = False
            self.app.setActiveMode(self.app.fontTagger)
            # self.onFontTagger = True
        # if clicked font explorer button
        if util.checkIfClickedButton(event.x, event.y, 
                        self.fontExplorerBtnCoords[0], self.fontExplorerBtnCoords[1], 
                        self.buttonWidth, self.buttonHeight):
            self.app.setActiveMode(self.app.fontExplorer)
            # self.onSplashPage = False
            # self.onFontExplorer = True

    '''
    View
    '''

    def createHeader(self, canvas):
        canvas.create_text(self.nameCoords[0], self.nameCoords[1], 
                            text="font organizer", font=("Red Hat Display Bold", 40))

    def createFontTaggerBtn(self, canvas):
        canvas.create_rectangle(self.fontTaggerBtnX[0], self.fontTaggerBtnY[0],
                                self.fontTaggerBtnX[1], self.fontTaggerBtnY[1])
        canvas.create_text(self.fontTaggerBtnCoords[0], self.fontTaggerBtnCoords[1],
                            text="font tagger", font=("Red Hat Display", 14))

    def createFontExplorerBtn(self, canvas):
        canvas.create_rectangle(self.fontExplorerBtnX[0], self.fontExplorerBtnY[0],
                                self.fontExplorerBtnX[1], self.fontExplorerBtnY[1])
        canvas.create_text(self.fontExplorerBtnCoords[0], self.fontExplorerBtnCoords[1], text="font explorer", font=("Red Hat Display", 15))

    def redrawAll(self, canvas):
    # def drawSplashPageUI(self, canvas):
        self.createHeader(canvas)
        self.createFontTaggerBtn(canvas)
        self.createFontExplorerBtn(canvas)
