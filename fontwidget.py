'''
This code is written by Kaylin Li. 
All code not written by Kaylin is credited next to the corresponding section.
'''

import win32gui
from tkinter import font
import tkinter as tk
from cmu_112_graphics import *

#import from other files
import utility as util

class FontWidget(Mode):
    def appStarted(self):
        self.widgetType = self.app.fontWidgetInfo[0]
        self.widgetText = self.app.fontWidgetInfo[5]
        self.fontSize = 24

        self.widgetFont = self.app.fontWidgetInfo[6]
        self.textStartY = 40

        self.textCursorIndex = len(self.widgetText)-1
        self.lineLength = len(self.widgetText)
        
    def keyPressed(self, event):
        text = self.widgetText
        print("yo")
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
        self.widgetText = text
        print("self.widgetText", self.widgetText)
    
    def drawBackButton(self, canvas):
        x = self.width-15
        y = 15
        width = 20
        height = 20
        canvas.create_rectangle(x-width/2, y-height/2, x+width/2, y+height/2)
        canvas.create_text(x,y, text="↰")

    def drawText(self, canvas):
        displayText = self.widgetText[:self.textCursorIndex] + "|" + self.widgetText[self.textCursorIndex:]
        canvas.create_rectangle(0,self.textStartY,self.width, self.height)
        tx0, ty0, tx1, ty1 = canvas.bbox(canvas.create_text(0,self.textStartY, 
                                        anchor="nw", text=displayText, font=(self.widgetFont,self.fontSize)))
        if (tx1>self.width):
            print("YOOOOOO")

    def redrawAll(self, canvas):
        self.drawBackButton(canvas)
        self.drawText(canvas)

