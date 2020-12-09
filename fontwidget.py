'''
File: fontwidget.py
Author: Kaylin Li
Purpose: creates a text-editor interface with the selected fonts from fontboard.py
All code not written by Kaylin is credited next to the corresponding section.
'''

import win32gui
from tkinter import font
import tkinter as tk
from cmu_112_graphics import *

import math
import copy

#import from other files
import utility as util

class FontWidget(Mode):
    def appStarted(self):
        # self.widgetType = self.app.fontWidgetInfo[0]

        # self.widgetText = self.app.fontWidgetInfo[5]
        self.widgetText = ["Headline", "Body Text"]
        self.fontSize = [24,24]
        self.widgetFont = [self.app.fontWidgetInfo[0][6], self.app.fontWidgetInfo[1][6]]
        self.fontWeight = ["normal", "normal"]

        self.activeTextBox = 0

        self.textStartY = 40
        self.averageCharWidth = [30, 30]
        self.maxCharsOnLine = [20, 20]

        self.textCursorIndex = len(self.widgetText[0])
        self.lineLength = len(self.widgetText[0])
        self.lineIndex = 0

        # button stuffs
        self.buttonDims = (20, 20) #dimensions
        self.saveButtonCoords = (self.width - 6*self.buttonDims[0], self.buttonDims[1] + 3)
        self.boldButtonCoords = (self.width - 4*self.buttonDims[0], self.buttonDims[1] + 3)
        self.italicButtonCoords = (self.width - 3*self.buttonDims[0], self.buttonDims[1] + 3)
        self.backButtonCoords = (self.width - self.buttonDims[0], self.buttonDims[1] + 3)

        self.time = 0
    
    def timerFired(self):
        if self.time == 0:
            self.time += 1

    def mousePressed(self, event):
        self.checkForBoldButton(event)
        self.checkForItalicButton(event)
        self.checkForBackButton(event)
        self.checkForSaveButton(event)
    
    def checkForSaveButton(self, event):
        if util.checkIfClickedButton(event.x, event.y, self.saveButtonCoords[0], self.saveButtonCoords[1], 
                                    self.buttonDims[0], self.buttonDims[1]):
            filename = self.widgetFont[0] + "and" + self.widgetFont[1]
            filename.replace(" ", "")
            self.app.saveSnapshot(f"fontboard/{filename}.png")
        

    def checkForBoldButton(self, event):
        if util.checkIfClickedButton(event.x, event.y, self.boldButtonCoords[0], self.boldButtonCoords[1], 
                                    self.buttonDims[0], self.buttonDims[1]):
            # font weight specifications taken from here: https://docs.python.org/3/library/tkinter.font.html
            if self.fontWeight[self.activeTextBox] == "normal":
                self.fontWeight[self.activeTextBox] = "bold"
            elif self.fontWeight[self.activeTextBox] == "italic":
                self.fontWeight[self.activeTextBox] = "bold italic"
            else:
                self.fontWeight[self.activeTextBox] = "normal"
    
    def checkForItalicButton(self, event):
        if util.checkIfClickedButton(event.x, event.y, self.italicButtonCoords[0], self.italicButtonCoords[1], 
                                    self.buttonDims[0], self.buttonDims[1]):
            if self.fontWeight[self.activeTextBox] == "normal":
                self.fontWeight[self.activeTextBox] = "italic"
            elif self.fontWeight[self.activeTextBox] == "bold":
                self.fontWeight[self.activeTextBox] = "bold italic"
            else:
                self.fontWeight[self.activeTextBox] = "normal"
    
    def checkForBackButton(self, event):
        if util.checkIfClickedButton(event.x, event.y, self.backButtonCoords[0], self.backButtonCoords[1], 
                                    self.buttonDims[0], self.buttonDims[1]):
            self.app.setActiveMode(self.app.fontBoard)
        
    def keyPressed(self, event):
        text = self.widgetText[self.activeTextBox]
        if event.key == "Backspace":
            text = text[:self.textCursorIndex-1]
            self.textCursorIndex -= 1
        elif event.key == "Space":
            text = text[:self.textCursorIndex] + " " + text[self.textCursorIndex:]
            self.textCursorIndex += 1
        else:
            text = text[:self.textCursorIndex] + event.key + text[self.textCursorIndex:]
            self.textCursorIndex += 1
        # text = text[:self.textCursorIndex] + "|" + text[self.textCursorIndex:]
        self.widgetText[self.activeTextBox] = text
        self.lineLength = len(text)
        # print("self.widgetText", self.widgetText)

    def drawMenuBar(self, canvas):
        self.drawFontName(canvas)
        self.drawSaveButton(canvas)
        self.drawBoldButton(canvas)
        self.drawItalicButton(canvas)
        self.drawBackButton(canvas)
        

    def drawFontName(self, canvas):
        canvas.create_text(0, 0, anchor="nw", text=f"{self.widgetFont[0]}, {self.widgetFont[1]}", font=("Red Hat Display", 20))

    def drawSaveButton(self, canvas):
        util.drawButton(self, canvas, self.saveButtonCoords, 
                    self.buttonDims[0], self.buttonDims[1], "Save")

    def drawBoldButton(self, canvas):
        util.drawButton(self, canvas, self.boldButtonCoords, 
                    self.buttonDims[0], self.buttonDims[1], "𝐁")

    def drawItalicButton(self, canvas):
        util.drawButton(self, canvas, self.italicButtonCoords, 
                    self.buttonDims[0], self.buttonDims[1], "𝐼")
    
    def drawBackButton(self, canvas):
        util.drawButton(self, canvas, self.backButtonCoords, 
                    self.buttonDims[0], self.buttonDims[1], "↰")
    
    def drawInitialText(self, canvas):
        canvas.create_rectangle(0, self.textStartY, self.width, self.height)
        print("yo")
        fontName = self.widgetFont[0]
        fontSize = self.fontSize[0]
        tx0, ty0, tx1, ty1 = canvas.bbox(canvas.create_text(0, self.textStartY, anchor="nw", 
                                        text=self.widgetText[0], font=(fontName, fontSize)))
        # try:
        averageCharWidth = ((tx1 - tx0) // len(self.widgetText[0]))
        # except:
            # averageCharWidth = 30
        self.maxCharsOnLine = (self.width // averageCharWidth)-5
        # print("self.maxCharsOnLine", self.maxCharsOnLine)

    def drawText(self, canvas):
        text0 = self.widgetText[0]
        displayText = text0[:self.textCursorIndex] + "|" + text0[self.textCursorIndex:]
        numLines = math.ceil(len(self.widgetText[0])//self.maxCharsOnLine)
        lineWidth = self.fontSize[0] + 5
        for lineNum in range(numLines+1):
            lineText = displayText[lineNum * self.maxCharsOnLine:(lineNum+1) * self.maxCharsOnLine]
            # print("lineText",lineText)
            canvas.create_text(0, self.textStartY + lineWidth * lineNum, anchor="nw", 
                                text=lineText, font=(self.widgetFont[0],self.fontSize[0],self.fontWeight[0]))

    def redrawAll(self, canvas):
        self.drawMenuBar(canvas)
        # rectangle for textbox
        canvas.create_rectangle(0, self.textStartY,self.width, self.height)
        if self.time <= 0:
            self.drawInitialText(canvas)
        else:
            self.drawText(canvas)




