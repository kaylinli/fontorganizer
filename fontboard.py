'''
File: fontboard.py
Author: Kaylin Li
Purpose: creates interface for constructing a font board
All code not written by Kaylin is credited next to the corresponding section.
'''
import win32gui
from tkinter import font
import tkinter as tk
from cmu_112_graphics import *

import random

# import other files
import utility as util

class FontBoard(Mode):
    '''
    Model
    '''
    def appStarted(self):
    # def initFEvars(self):
        # list of widgets in the format 
        #           0           1  2   3   4      5         6       8
        # [boolForWidgetType, x0, y0, x1, y1, widgetText, font, fontSize]

        self.marginLeft = 10
        self.fontNames = self.app.fontNames

        self.interactionBar = 65

        self.fontsAndTagsSelected = set()

        self.boardButtonDims = (90, 20) # dimensions of button
        self.boardButtonCoords = (self.width - 10 - self.boardButtonDims[0]/2,
                                    self.interactionBar*(2/3))

        self.searchBarWidth = 120
        self.searchBarHeight = 20
        self.searchBarCoords = (self.width - 10 - self.searchBarWidth/2,
                                    self.interactionBar)
        self.isTypingSearch = False
        self.searchBarInput = ""
        self.selectedFontsAndTags = set()
        self.relatedFonts = []

        self.widgets = []
        self.widgetFonts = self.fontNames
        self.selectedWidget = [-1,-1]
        self.widgetWidth = 150
        self.widgetHeight = 30
        self.widgetStartX = self.marginLeft
        self.widgetStartY = 80

        self.app.fontWidgetInfo = [[],[]]
        
        self.findAllRelatedFonts()
        self.createWidgets()
        

    def createWidgets(self):
        # width = random.randrange(100,200)
        # height = random.randrange(100,200)
        while not (self.widgetStartX > self.width or self.widgetStartY > self.height):
            x0, y0, x1, y1 = (self.widgetStartX, self.widgetStartY, 
                            self.widgetStartX + self.widgetWidth, self.widgetStartY + self.widgetHeight)
            self.createTextWidget(x0, y0, x1, y1)

            # lastIndex = len(self.widgets)-1
            # x0, y0, x1, y1 = self.widgets[lastIndex]
            # createTextWidget(self, x0, y0, x1, y1)

            tempX = self.widgetStartX
            tempY = self.widgetStartY 

            self.widgetStartX += self.widgetWidth + 10
            
            if self.widgetStartX + self.widgetWidth >= self.width and \
                    self.widgetStartY + self.widgetHeight >= self.height:
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
        if len(self.selectedFontsAndTags) > 0:
            font = random.choice(self.relatedFonts)
        else:
            font = random.choice(self.widgetFonts)
        self.widgets += [[0, x0, y0, x1, y1, "Hello", font, 15]]
    
    def findAllRelatedFonts(self):
        for tag in self.selectedFontsAndTags:
            for font in self.fontTags:
                if tag in self.fontTags[font]:
                    self.relatedFonts += font

    '''
    Controller
    '''
    def mousePressed(self, event):
        self.checkForClickedBoardButton(event)
        self.checkForClickedSearchBar(event)
        self.checkForSelectedWidget(event)

    def checkForClickedBoardButton(self, event):
        if util.checkIfClickedButton(event.x, event.y, 
                                    self.boardButtonCoords[0], self.boardButtonCoords[1], 
                                    self.boardButtonDims[0], self.boardButtonDims[1]):
            self.app.setActiveMode(self.app.Board)

    def checkForSelectedWidget(self, event):
        for i in range(len(self.widgets)):
            widget = self.widgets[i]
            # check if within widget bounds
            if widget[1] < event.x < widget[3] and \
                    widget[2] < event.y < widget[4]:
                if self.selectedWidget[0] == -1:
                    self.selectedWidget[0] = i
                    self.app.fontWidgetInfo[0] = widget
                else:
                    self.selectedWidget[1] = i
                    self.app.fontWidgetInfo[1] = widget
                if (self.selectedWidget[0] != -1 and self.selectedWidget[1] != -1):
                    self.app.setActiveMode(self.app.fontWidget)
                    self.app.fontWidget.appStarted()
                    self.selectedWidget = [-1,-1]
                # return
        # if no widget selected
        

    def checkForClickedSearchBar(self, event):
        if util.checkIfClickedButton(event.x, event.y, 
                                    self.searchBarCoords[0], self.searchBarCoords[1], 
                                    self.searchBarWidth, self.searchBarHeight):
            self.isTypingSearch = True
            return
        else:
            self.isTypingSearch = False
            

    def keyPressed(self, event):
        # self.checkForWidgetInput( event)
        self.checkForSearchInput(event)

    def checkForSearchInput(self, event):
        if self.isTypingSearch:
            if event.key == "Enter":
                for value in self.app.fontTags.values():
                    if self.searchBarInput.lower().strip() in value:
                        self.selectedFontsAndTags.add(self.searchBarInput.lower().strip())
                        print(self.selectedFontsAndTags)
                        self.widgets = []
                        self.createWidgets()
            else:
                self.searchBarInput = util.checkForInput(self, event, self.searchBarInput)
        

    def checkForWidgetInput(self, event):
        if self.selectedWidget != -1:
            self.widgets[self.selectedWidget][5] = util.checkForInput(self, event, 
                                            self.widgets[self.selectedWidget][5])
        
    '''
    View
    '''

    def drawWidgets(self, canvas):
        for i in range(len(self.widgets)):
            widget = self.widgets[i]
            wx0, wy0, wx1, wy1 = widget[1], widget[2], widget[3], widget[4]
            # canvas.create_rectangle(wx0, wy0, wx1, wy1)
            # widgetText = self.widgets[i][5]
            fontName = self.widgets[i][6]
            fontSize = self.widgets[i][7]
            tx0, ty0, tx1, ty1 = canvas.bbox(canvas.create_text(wx0 + 10, wy0 + 10, 
                                    text=self.widgets[i][6], anchor="nw",font=(fontName, fontSize)))

    def createHeader(self, canvas):
        canvas.create_text(self.marginLeft, 30, text="font board", anchor="w", font=("Red Hat Display Medium", 24))
        self.drawTagsSelected(canvas)
        self.drawBoardButton(canvas)
        self.drawSearchBar(canvas)
    
    def drawTagsSelected(self, canvas):
        selectionX = self.marginLeft + 100
        selectionWidth = 50
        canvas.create_text(self.marginLeft, self.interactionBar, anchor="w", text="tags selected: ")
        i = 0
        for tag in self.selectedFontsAndTags:
            canvas.create_text(selectionX + i*50, self.interactionBar, anchor="w", text=tag)
            i += 1

    def drawBoardButton(self, canvas):
        util.drawButton(self, canvas, self.boardButtonCoords, 
                        self.boardButtonDims[0], self.boardButtonDims[1], "see font board")

    def drawSearchBar(self, canvas):
        canvas.create_rectangle(self.searchBarCoords[0] - self.searchBarWidth/2,
                                self.searchBarCoords[1] - self.searchBarHeight/2,
                                self.searchBarCoords[0] + self.searchBarWidth/2,
                                self.searchBarCoords[1] + self.searchBarHeight/2)

        searchBarText = ""
        if self.searchBarInput == "" and self.isTypingSearch == False:
            searchBarText = "search for a font/tag and press Enter"
        else:
            searchBarText = self.searchBarInput
        canvas.create_text(self.searchBarCoords[0], self.searchBarCoords[1], text=searchBarText)

    def redrawAll(self, canvas):
    # def drawFontExplorerUI(self, canvas):
        self.createHeader(canvas)
        self.drawWidgets(canvas)
