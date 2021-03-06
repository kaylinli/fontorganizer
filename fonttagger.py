'''
File: fonttagger.py
Author: Kaylin Li
Purpose: creates interface for tagging fonts with attributes
All code not written by Kaylin is credited next to the corresponding section.
'''

import math
import win32gui
from tkinter import font
import tkinter as tk
from cmu_112_graphics import *

# import other files
import utility as util
import autofonttagger as at

class FontTagger(Mode):

    '''
    Model
    '''

    def appStarted(self):
    # def initFTvars(self):
        # layout stuff
        self.fontNames = self.app.fontNames
        self.marginLeft = 10
        self.headerWidth = 70
        self.startEntries = 80 # y position of where the entries start
        self.entryHeight = 20 # space between entries
        self.entryMarginLeft = self.marginLeft + 20

        # page stuff
        self.fontEntries = (self.height-self.headerWidth)//20 - 2# number of entries on a page
        self.pageNum = 0 # page number starts at 0
        self.totalPages = len(self.fontNames) // self.fontEntries


        # NOTE: all "coordinate" variables represent the center of the object


        # Header Vars
        # tag input variables
        self.tagInputCoords = (self.marginLeft+50, 65) # coords for middle of box
        self.tagInputX = (self.marginLeft, self.marginLeft+100)
        self.tagInputY = 55, 55+20
        self.isTypingTag = False
        self.tagInput = ""

        self.tagButtonWidth = 60
        self.tagButtonHeight = 20
        self.tagButtonCoords = (self.tagInputX[1]+self.tagButtonWidth/2, 
                                self.tagInputCoords[1])

        self.backButtonDims = (20, 20)
        self.backButtonCoords = (self.width - 10 - self.backButtonDims[0]/2, 
                                self.tagInputCoords[1]*(1/3))

        self.autoTagButtonWidth = 90
        self.autoTagButtonHeight = 20
        self.autoTagButtonCoords = (self.width - 10 - self.autoTagButtonWidth/2,
                                    self.tagInputCoords[1]*(2/3))

        self.searchButtonWidth = 90
        self.searchButtonHeight = 20
        self.searchButtonCoords = (self.width - 10 - self.searchButtonWidth/2, 
                                    self.tagInputCoords[1])

        self.selectionBoxSize = 10
        self.selectedFonts = set()
        
        # variables for page navigation
        self.forwardButtonX = self.width/2 + 20
        self.forwardButtonY = self.height - 10
        self.backButtonX = self.width/2 - 20
        self.backButtonY = self.height - 10

        # self.initializeFontTags()d

    

    # def initializeFontTags(self):
    #     file = ""
    #     try: # if the file doesn't exist, create one
    #         # https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/
    #         file = open("fonttags.txt", "x")
    #         for font in self.fontNames:
    #             file.write(f"{font}: \n")
    #     except:
    #         file = open("fonttags.txt", "r")
    #         data = file.read()
    #         for line in file:
    #             # example line: "Arial: Sans serif, project1"
    #             colonIndex = line.find(":")
    #             font = line[:colonIndex]
    #             tags = line[colonIndex:].split(", ")
    #             for tag in tags:
    #                 self.app.fontTags[font] += [tag]

    # def appStopped(self):

    '''
    Controller
    '''

    def mousePressed(self, event):
        # top
        self.checkForTagInput(event)
        self.checkForBackButton(event)
        self.checkForTagButton(event)
        self.checkForAutoTagButton(event)
        # middle
        self.checkForSelectedBoxes(event)
        # bottom
        self.checkForNavigation(event)

    # checks if user has typed in a tag name
    def checkForTagInput(self,event):
        if util.checkIfClickedButton(event.x, event.y, 
                        self.tagInputCoords[0],self.tagInputCoords[1], 100, 20):
            self.isTypingTag = True
            self.isTypingTag = True
        else:
            self.isTypingTag = False
        # TODO: check if 'x' button was clicked to clear tag input

    # check if user is trying to tag selected fonts
    def checkForTagButton(self, event):
        if util.checkIfClickedButton(event.x, event.y, 
                        self.tagButtonCoords[0], #cx
                        self.tagButtonCoords[1], #cy
                        self.tagButtonWidth, self.tagButtonHeight):
            print("recognized button click")
            if self.selectedFonts != set():
                print("fonts added to selected fonts")
                for font in self.selectedFonts:
                    self.tagInput = self.tagInput.strip()
                    if font not in self.app.fontTags:
                        self.app.fontTags[font] = [self.tagInput]
                    elif self.tagInput not in self.app.fontTags[font]:
                        self.app.fontTags[font] += [self.tagInput]
                    print(font, self.app.fontTags[font])
            util.saveTagsToComputer(self)

    def checkForBackButton(self, event):
        if util.checkIfClickedButton(event.x, event.y, 
                        self.backButtonCoords[0], #cx
                        self.backButtonCoords[1], #cy
                        self.backButtonDims[0], self.backButtonDims[1]):
            self.app.setActiveMode(self.app.splashPage)

    def checkForAutoTagButton(self, event):
        if util.checkIfClickedButton(event.x, event.y, 
                        self.autoTagButtonCoords[0], #cx
                        self.autoTagButtonCoords[1], #cy
                        self.autoTagButtonWidth, self.autoTagButtonHeight):
            # autoFontTags = at.AutoFontTagger(width=150, height=150)
            self.app.setActiveMode(self.app.autoFontTagger)

    def checkForSelectedBoxes(self, event):
        # if they've clicked somewhere within the selected boxes area
        if (self.marginLeft < event.x < self.marginLeft + self.selectionBoxSize) and \
                (self.startEntries < event.y < self.startEntries + self.fontEntries*self.entryHeight):
            boxIndex = math.floor((event.y - self.startEntries - self.entryHeight/2) / self.entryHeight)
            boxIndex += self.pageNum * self.fontEntries
            font = self.fontNames[boxIndex]
            if font in self.selectedFonts:
                self.selectedFonts.remove(font)
            else:
                self.selectedFonts.add(font)

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
            if event.key == "Backspace":
                self.tagInput = self.tagInput[:len(self.tagInput)-1]
            elif event.key == "Space":
                self.tagInput += " "
            else:
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
                self.createEntry(canvas, fontFamily, currentHeight)
            except Exception as e:
                print(e)
                print(fontFamily)
            currentHeight += self.entryHeight

    def createEntry(self, canvas, fontFamily, currentHeight):
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
        tx0, ty0, tx1, ty1 = canvas.bbox(canvas.create_text(self.entryMarginLeft, currentHeight, anchor='w', 
                            text=f'{fontFamily}', font=fontType))

        px1 = tx1 + 10
        if fontFamily in self.app.fontTags:
            for i in range(len(self.app.fontTags[fontFamily])):
                tag = self.app.fontTags[fontFamily][i]
                px0, py0, px1, py1 = canvas.bbox(canvas.create_text(px1+20, currentHeight, anchor='w', 
                            text=tag, fill="grey"))
                canvas.create_rectangle(px0, py0, px1, py1)
        

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
        
        self.drawTagInputBox(canvas)
        self.drawTagButton(canvas)
        self.drawAutoTaggingButton(canvas)
        self.drawSearchButton(canvas)
        self.drawBackButton(canvas)

    def drawTagInputBox(self, canvas):
        # create box
        x0, x1 = self.tagInputX[0], self.tagInputX[1]
        y0, y1 = self.tagInputY[0], self.tagInputY[1]
        canvas.create_rectangle(x0, y0, x1, y1)

        # create text inside box
        # TODO: make text wrap around if it goes outside box'
        # TODO: allow for Backspace, Enter, Left and Right functionality
        if self.tagInput == "" and self.isTypingTag == False:
            canvas.create_text(x0+5, y0+3, anchor="nw", text="type tag here", fill="grey")
        else: # if self.isTypingTag == True
            canvas.create_text(x0+5, y0+3, anchor="nw", text=f"{self.tagInput}")

    def drawTagButton(self, canvas):
        util.drawButton(self, canvas, self.tagButtonCoords, 
                        self.tagButtonWidth, self.tagButtonHeight, "tag fonts")
    
    def drawBackButton(self, canvas):
        util.drawButton(self, canvas, self.backButtonCoords, 
                    self.backButtonDims[0], self.backButtonDims[1], "↰")

    def drawAutoTaggingButton(self, canvas):
        util.drawButton(self, canvas, self.autoTagButtonCoords, 
                        self.autoTagButtonWidth, self.autoTagButtonHeight, "auto tag fonts")

    def drawSearchButton(self, canvas):
        util.drawButton(self, canvas, self.searchButtonCoords, 
                        self.searchButtonWidth, self.searchButtonHeight, 
                        "search for a font")

    


    # draws the entire font tagger page
    def redrawAll(self, canvas):
    # def drawFontTaggerUI(self, canvas):
        self.pageSetup(canvas)
        self.createHeader(canvas)
        self.createNavigationButtons(canvas)

