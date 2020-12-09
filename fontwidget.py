'''
This code is written by Kaylin Li. 
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
        self.widgetText = "Headline"
        self.fontSize = 24
        self.widgetFont = self.app.fontWidgetInfo[0][6]
        self.fontWeight = "normal"


        self.textStartY = 40
        self.averageCharWidth = 30
        self.maxCharsOnLine = 20

        self.textCursorIndex = len(self.widgetText)
        self.lineLength = len(self.widgetText)
        self.lineIndex = 0

        # button stuffs
        self.buttonDims = (20, 20) #dimensions
        self.boldButtonCoords = (self.width - 4*self.buttonDims[0], self.buttonDims[1] + 3)
        self.italicButtonCoords = (self.width - 3*self.buttonDims[0], self.buttonDims[1] + 3)
        self.backButtonCoords = (self.width - self.buttonDims[0], self.buttonDims[1] + 3)

        self.time = 0
    
    def timerFired(self):
        if self.time == 0:
            self.time += 1

    def mousePressed(self, event):
        self.checkForClickedButton(event)
    

    def checkForClickedButton(self, event):
        
        if util.checkIfClickedButton(event.x, event.y, self.boldButtonCoords[0], self.boldButtonCoords[1], 
                                    self.buttonDims[0], self.buttonDims[1]):
            # font weight specifications taken from here: https://docs.python.org/3/library/tkinter.font.html
            if self.fontWeight == "normal":
                self.fontWeight = "bold"
            elif self.fontWeight == "italic":
                self.fontWeight = "bold italic"
            else:
                self.fontWeight = "normal"

        if util.checkIfClickedButton(event.x, event.y, self.italicButtonCoords[0], self.italicButtonCoords[1], 
                                    self.buttonDims[0], self.buttonDims[1]):
            if self.fontWeight == "normal":
                self.fontWeight = "italic"
            elif self.fontWeight == "bold":
                self.fontWeight = "bold italic"
            else:
                self.fontWeight = "normal"

        if util.checkIfClickedButton(event.x, event.y, self.backButtonCoords[0], self.backButtonCoords[1], 
                                    self.buttonDims[0], self.buttonDims[1]):
            self.app.setActiveMode(self.app.fontBoard)
        
    def keyPressed(self, event):
        text = self.widgetText
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
        self.widgetText= text
        self.lineLength = len(text)
        # print("self.widgetText", self.widgetText)

    def drawMenuBar(self, canvas):
        self.drawFontName(canvas)
        self.drawBoldButton(canvas)
        self.drawItalicButton(canvas)
        self.drawBackButton(canvas)
        

    def drawFontName(self, canvas):
        canvas.create_text(0, 0, anchor="nw", text=self.widgetFont, font=("Red Hat Display", 24))

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
        canvas.create_rectangle(0, self.textStartY,self.width, self.height)
        tx0, ty0, tx1, ty1 = canvas.bbox(canvas.create_text(0, self.textStartY, anchor="nw", 
                                        text=self.widgetText, font=(self.widgetFont,self.fontSize)))
        try:
            averageCharWidth = ((tx1 - tx0) // len(self.widgetText))
        except:
            averageCharWidth = 30
        self.maxCharsOnLine = (self.width // averageCharWidth)-5
        # print("self.maxCharsOnLine", self.maxCharsOnLine)

    def drawText(self, canvas):
        displayText = self.widgetText[:self.textCursorIndex] + "|" + self.widgetText[self.textCursorIndex:]
        canvas.create_rectangle(0, self.textStartY,self.width, self.height)
        numLines = math.ceil(len(self.widgetText)//self.maxCharsOnLine)
        lineWidth = self.fontSize + 5
        for lineNum in range(numLines+1):
            lineText = displayText[lineNum * self.maxCharsOnLine:(lineNum+1) * self.maxCharsOnLine]
            # print("lineText",lineText)
            canvas.create_text(0, self.textStartY + lineWidth * lineNum, anchor="nw", 
                                text=lineText, font=(self.widgetFont,self.fontSize,self.fontWeight))

    def redrawAll(self, canvas):
        self.drawMenuBar(canvas)
        if self.time <= 0:
            self.drawInitialText(canvas)
        else:
            self.drawText(canvas)




