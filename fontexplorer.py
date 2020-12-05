import win32gui
from tkinter import font
import tkinter as tk
from cmu_112_graphics import *

import random

# import other files
import utility as util

class FontExplorer(Mode):
    '''
    Model
    '''
    def appStarted(self):
    # def initFEvars(self):
        # list of widgets in the format 
        #           0           1  2   3   4      5         6       7
        # [boolForWidgetType, x0, y0, x1, y1, widgetText, font, textlines]

        self.marginLeft = 10
        self.fontNames = self.app.fontNames


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
        self.isTypingSearch = False
        self.searchBarInput = ""

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
        fontIndex = random.randrange(0, len(self.fontNames))
        self.widgets += [[0, x0, y0, x1, y1, "Click to edit", self.fontNames[fontIndex], 1]]
    '''
    Controller
    '''
    def mousePressed(self, event):
        self.checkForSelectedWidget(event)
        self.checkForClickedSearchBar(event)

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

    def checkForClickedSearchBar(self, event):
        if util.checkIfClickedButton(event.x, event.y, 
                                    self.searchBarCoords[0], self.searchBarCoords[1], 
                                    self.searchBarWidth, self.searchBarHeight):
            self.isTypingSearch = True
        else:
            self.isTypingSearch = False
            

    def keyPressed(self, event):
        self.checkForWidgetInput( event)

    def checkForSearchInput(self, event):
        if self.isTypingSearch:
            print("checking for input")
            self.searchBarInput = util.checkForInput(self, event, self.searchBarInput)

    def checkForWidgetInput(self, event):
        if self.selectedWidget != -1:
            self.widgets[self.selectedWidget][5] = util.checkForInput(self, event, 
                                            self.widgets[self.selectedWidget][5])
            # widgetText = self.widgets[self.selectedWidget][5]
            # if event.key == "Backspace":
            #     widgetText = widgetText[:len(widgetText)-1]
            # elif event.key == "Space":
            #     widgetText += " "
            # else:
            #     widgetText += event.key 
            # self.widgets[self.selectedWidget][5] = widgetText
        
    '''
    View
    '''

    def drawWidgets(self, canvas):
        for i in range(len(self.widgets)):
            widget = self.widgets[i]
            wx0, wy0, wx1, wy1 = widget[1], widget[2], widget[3], widget[4]
            canvas.create_rectangle(wx0, wy0, wx1, wy1)
            widgetText = self.widgets[i][5]
            
            lineWidth = 15
            # lineX = (wx0+wx1)/2
            # lineY = (wy0+wy1)/2 - (widget[7]/2)*lineWidth
            lineX = wx0 + 10
            lineY = wy0 + 10
            index = 0
            lineLength = len(widgetText)
            # create lines of text in widget
            while index < len(widgetText):
                lineText = widgetText[index:lineLength]
                lineY += lineWidth
                tx0, ty0, tx1, ty1 = (canvas.bbox(canvas.create_text(lineX, lineY, 
                                text=lineText, anchor="w",font=(self.widgets[i][6], 15))))
                canvas.create_rectangle(tx0, ty0, tx1, ty1)
                if tx1 > wx1:
                    print("over")
                    lineLength -= 1
                    widget[7] += 1
                index += lineLength

            # canvas.create_oval(x0,y0,x1,y1)
            # drawTextWidget(self, canvas, i, widget[1], widget[1], )

    # def drawTextWidget(self, canvas, widgetNum, x0, y0, x1, y1):
    #     canvas.create_rectangle(x0, y0, x1, y1)
    #     canvas.create_text((x0+x1)/2, (y0+y1)/2, text=self.widgets[widgetNum][5])

    def createHeader(self, canvas):
        canvas.create_text(self.marginLeft, 30, text="font explorer", anchor="w", font=("Red Hat Display Medium", 24))
        self.drawSearchBar(canvas)

    def drawSearchBar(self, canvas):
        canvas.create_rectangle(self.searchBarCoords[0] - self.searchBarWidth/2,
                                self.searchBarCoords[1] - self.searchBarHeight/2,
                                self.searchBarCoords[0] + self.searchBarWidth/2,
                                self.searchBarCoords[1] + self.searchBarHeight/2)

        searchBarText = ""
        if self.searchBarInput == "" and self.isTypingSearch == False:
            searchBarText = "search for a font/tag"
        else:
            searchBarText = self.searchBarInput
        canvas.create_text(self.searchBarCoords[0], self.searchBarCoords[1], text=searchBarText)

    def redrawAll(self, canvas):
    # def drawFontExplorerUI(self, canvas):
        self.createHeader(canvas)
        self.drawWidgets(canvas)
