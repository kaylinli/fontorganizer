import win32gui
from tkinter import font
import tkinter as tk
from cmu_112_graphics import *

import random

# import other files
import utility as util

'''
Model
'''

def initFEvars(self):
    # list of widgets in the format 
    #           0           1  2   3   4      5         6       7
    # [boolForWidgetType, x0, y0, x1, y1, widgetText, font, textlines]
    self.widgets = []
    self.selectedWidget = -1

    self.interactionBar = 65

    
    self.widgetWidth = 150
    self.widgetHeight = 100

    self.widgetStartX = self.marginLeft
    self.widgetStartY = 80

    self.searchBarWidth = 60
    self.searchBarHeight = 20
    self.searchBarCoords = (self.width - 10 - self.searchBarWidth/2,
                                self.interactionBar)

    createWidgets(self)

def createWidgets(self):
    # width = random.randrange(100,200)
    # height = random.randrange(100,200)
    while not (self.widgetStartX > self.width or self.widgetStartY > self.height):
        x0, y0, x1, y1 = (self.widgetStartX, self.widgetStartY, 
                        self.widgetStartX + self.widgetWidth, self.widgetStartY + self.widgetHeight)
        createTextWidget(self, x0, y0, x1, y1)

        # lastIndex = len(self.widgets)-1
        # x0, y0, x1, y1 = self.widgets[lastIndex]
        # createTextWidget(self, x0, y0, x1, y1)

        tempX = self.widgetStartX
        tempY = self.widgetStartY 

        self.widgetStartX += self.widgetWidth + 10
        
        if self.widgetStartX + self.widgetWidth > self.width and \
                self.widgetStartY + self.widgetHeight> self.height:
            self.widgetStartX = tempX
            self.widgetStartY = tempY
            return
        if self.widgetStartX > self.width: # if it goes off the screen, reverse
            self.widgetStartX = self.marginLeft
            self.widgetStartY += self.widgetHeight + 10
        elif self.widgetStartY > self.height:
            self.widgetStartY = tempX
        
        if tempX == self.widgetStartX and tempY == self.widgetStartY:
            return


def createTextWidget(self, x0, y0, x1, y1):
    fontIndex = random.randrange(0, len(self.fontNames))
    self.widgets += [[0, x0, y0, x1, y1, "Click to edit", self.fontNames[fontIndex]], 1]
'''
Controller
'''
def mousePressed(self, event):
    checkForSelectedWidget(self, event)

def checkForSelectedWidget(self, event):
    for i in range(len(self.widgets)):
        widget = self.widgets[i]
        # check if within widget bounds
        if widget[1] < event.x < widget[3] and \
            widget[2] < event.y < widget[4]:
            self.selectedWidget = i
            return
    # if no widget selected
    self.selectedWidget = -1
    

def keyPressed(self, event):
    if self.selectedWidget != -1:
        self.widgets[self.selectedWidget][5] += event.key 
'''
View
'''

def drawWidgets(self, canvas):
    for i in range(len(self.widgets)):
        widget = self.widgets[i]
        wx0, wy0, wx1, wy1 = widget[1], widget[2], widget[3], widget[4]
        canvas.create_rectangle(wx0, wy0, wx1, wy1)
        widgetText = self.widgets[i][5]
        tx0, ty0, tx1, ty1 = (canvas.bbox(canvas.create_text((x0+x1)/2, (y0+y1)/2, 
                        text=widgetText, font=(self.widgets[i][6], 15))))
        if ty1 > wy1:
             canvas.create_text()
        canvas.create_text((x0+x1)/2, (y0+y1)/2 + 20, 
                        text=widgetText, font=(self.widgets[i][6], 15))
        # canvas.create_oval(x0,y0,x1,y1)
        # drawTextWidget(self, canvas, i, widget[1], widget[1], )

# def drawTextWidget(self, canvas, widgetNum, x0, y0, x1, y1):
#     canvas.create_rectangle(x0, y0, x1, y1)
#     canvas.create_text((x0+x1)/2, (y0+y1)/2, text=self.widgets[widgetNum][5])

def createHeader(self, canvas):
    canvas.create_text(self.marginLeft, 30, text="font explorer", anchor="w", font=("Red Hat Display Medium", 24))
    drawSearchBar(self, canvas)

def drawSearchBar(self, canvas):
    canvas.create_rectangle(self.searchBarCoords[0] - self.searchBarWidth/2,
                            self.searchBarCoords[1] - self.searchBarHeight/2,
                            self.searchBarCoords[0] + self.searchBarWidth/2,
                            self.searchBarCoords[1] + self.searchBarHeight/2)

def drawFontExplorerUI(self, canvas):
    createHeader(self, canvas)
    drawWidgets(self, canvas)
