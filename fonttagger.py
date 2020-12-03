'''
This code is written by Kaylin Li. 
All code not written by Kaylin is credited next to the corresponding section.
'''

import math
import win32gui
from tkinter import font
import tkinter as tk
from cmu_112_graphics import *

# import other files
import utility as util

'''
Model
'''

def initFTvars(self):
    # layout stuff
    self.marginLeft = 10
    self.headerWidth = 70
    self.startEntries = 80 # y position of where the entries start
    self.entryHeight = 20 # space between entries
    self.entryMarginLeft = self.marginLeft + 20

    # page stuff
    self.fontEntries = (self.height-self.headerWidth)//20 - 2# number of entries on a page
    self.pageNum = 0 # page number starts at 0
    self.totalPages = len(self.fontNames) // self.fontEntries


    # tag input variables
    self.tagInputCoords = (self.marginLeft+50, 65)
    self.tagInputX = (self.marginLeft, self.marginLeft+100)
    self.tagInputY = 55, 55+20
    self.isTypingTag = False
    self.tagInput = ""

    self.selectionBoxSize = 10
    self.selectedFonts = set()
    
    # variables for page navigation
    self.forwardButtonX = self.width/2 + 20
    self.forwardButtonY = self.height - 10
    self.backButtonX = self.width/2 - 20
    self.backButtonY = self.height - 10

'''
Controller
'''

def mousePressed(self, event):
    checkForTagInput(self, event)
    checkForSelectedBoxes(self, event)
    checkForNavigation(self, event)

# checks if user has typed in a tag name
def checkForTagInput(self,event):
    if util.checkIfClickedButton(event.x, event.y, 
                    self.tagInputCoords[0],self.tagInputCoords[1], 100, 20):
        self.isTypingTag = True
        self.isTypingTag = True
    else:
        self.isTypingTag = False
    # TODO: check if 'x' button was clicked to clear tag input

def checkForSelectedBoxes(self, event):
    # if they've clicked somewhere within the selected boxes area
    if (self.marginLeft < event.x < self.marginLeft + self.selectionBoxSize) and \
            (self.startEntries < event.y < self.startEntries + self.fontEntries*self.entryHeight):
        boxIndex = math.floor((event.y - self.startEntries) / self.entryHeight)
        boxIndex += self.pageNum * self.fontEntries
        self.selectedFonts.add(self.fontNames[boxIndex])

# checks if navigation buttons are pressed
def checkForNavigation(self, event):
    if util.checkIfClickedButton(event.x, event.y, 
                self.forwardButtonX, self.forwardButtonY, 20, 20):
        self.pageNum += 1
    if util.checkIfClickedButton(event.x, event.y, 
                self.backButtonX, self.backButtonY, 20, 20):
        # if self.pageNum != 0: disables back button on 0th page
        self.pageNum -= 1
    self.pageNum = self.pageNum % self.totalPages

def keyPressed(self, event):
    if self.isTypingTag:
        self.tagInput += event.key 

'''
View
'''

# sets up a page of fonts
def pageSetup(self, canvas):
    currentHeight = self.startEntries + self.entryHeight
    firstEntry = self.pageNum * self.fontEntries
    for fontFamily in self.fontNames[firstEntry:(firstEntry+self.fontEntries)]:
        try:
            # prevents issues with spaces in font name
            fontType = font.Font(family=fontFamily,size=14)
            # create 10px by 10px selection box
            canvas.create_rectangle(self.marginLeft,         currentHeight - self.selectionBoxSize/2, 
                    self.marginLeft + self.selectionBoxSize, currentHeight + self.selectionBoxSize/2)
            # if the font is selected, add a checkmark
            if fontFamily in self.selectedFonts:
                canvas.create_text(self.marginLeft + self.selectionBoxSize/2, 
                                    currentHeight, text="✓")
            # create text with font name
            canvas.create_text(self.entryMarginLeft, currentHeight, anchor='w', 
                                text=f'{fontFamily}', font=fontType)
        except Exception as e:
            print(e)
            print(fontFamily)
        currentHeight += self.entryHeight

def createNavigationButtons(self,canvas):
    # TODO: add buttons to jump to a page, or have  |<| |1| |2| ... |20| |>| 
    # inspo: https://cdn2.vectorstock.com/i/1000x1000/47/91/pagination-bar-page-navigation-web-buttons-vector-22654791.jpg
    # inspo2: https://cdn4.vectorstock.com/i/1000x1000/47/88/pagination-bar-page-navigation-web-buttons-vector-22654788.jpg
    canvas.create_rectangle(self.forwardButtonX-10, self.forwardButtonY-10, self.forwardButtonX+10,self.forwardButtonY+10)
    canvas.create_rectangle(self.backButtonX-10, self.backButtonY-10, self.backButtonX+10,self.backButtonY+10)
    canvas.create_text(self.forwardButtonX, self.forwardButtonY, text='>')
    canvas.create_text(self.backButtonX, self.backButtonY, text='<')

def createHeader(self, canvas):
    canvas.create_text(self.marginLeft, 30, text="font tagger", anchor="w", font=("Red Hat Display Medium", 24))
    
    drawTagInputBox(self, canvas)

def drawTagInputBox(self, canvas):
    # create box
    x0, x1 = self.tagInputX[0], self.tagInputX[1]
    y0, y1 = self.tagInputY[0], self.tagInputY[1]
    canvas.create_rectangle(x0, y0, x1, y1)

    # create text inside box
    # TODO: make text wrap around if it goes outside box'
    if self.tagInput == "" and self.isTypingTag == False:
        canvas.create_text(x0+5, y0+3, anchor="nw", text="type tag here")
    else: # if self.isTypingTag == True
        canvas.create_text(x0+5, y0+3, anchor="nw", text=f"{self.tagInput}")

    # create clear button
    x0, x1 = self.tagInputX[1]+10, self.tagInputX[1]+30
    y0, y1 = self.tagInputY[0], self.tagInputY[0]+20
    canvas.create_rectangle(x0, y0, x1, y1)
    canvas.create_text(x0+10, y0+10, anchor="center", text="×", font=("Red Hat Display", 14))

# draws the entire font tagger page
def drawFontTaggerUI(self, canvas):
    pageSetup(self, canvas)
    createHeader(self,canvas)
    createNavigationButtons(self,canvas)

'''
Generic Utility Functions
'''

