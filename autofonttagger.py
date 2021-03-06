'''
File: autofonttagger.py
Author: Kaylin Li
Purpose: displays mode that automatically tags font displayed as either serif, sans serif, or handwriting
All code not written by Kaylin is credited next to the corresponding section.
'''
import sys
import math
import cv2 as cv
import numpy as np

import win32gui
from tkinter import font
import tkinter as tk
from cmu_112_graphics import *

def callback(font, tm, fonttype, names):
    names.append(font.lfFaceName)
    return True

fontNames = []
hdc = win32gui.GetDC(None)
win32gui.EnumFontFamilies(hdc, None, callback, fontNames)
# print("\n".join(fontnames))
fontNames = sorted(fontNames)
# print(fontNames)
win32gui.ReleaseDC(hdc, None)
# the above code is from https://stackoverflow.com/questions/51256688/python-windows-enum-installed-fonts

from cmu_112_graphics import *
import fonttagger as ft
import utility as util

class AutoFontTagger(Mode):

    def appStarted(self):
        self.fontNames = fontNames
        self.fontIndex = 0
        self.image = None
        self.hasSerif = False
        self.timerDelay = 1
        # self.fontTags = dict()

    def timerFired(self):
        if self.fontIndex < len(fontNames)-1:
            # util.saveTagsToComputer(self)
            util.saveTagsToComputer(self)
            self.fontIndex += 1
        else:
            util.saveTagsToComputer(self)
            self.app.setActiveMode(self.app.fontTagger)
        snapshotImage = self.app.getSnapshot()
        self.app.saveSnapshot("n.png")
        font = self.fontNames[self.fontIndex]

        tag = self.fontHasSerif()
        # if tag not in self.app.fontTags[font]:
        if font in self.app.fontTags:
            self.app.fontTags[font] += [tag]
        else:
            self.app.fontTags[font] = [tag]
        # self.image = self.scaleImage(snapshotImage, 0.4)
    
    # def appStopped(self):
    #     return self.fontTags
    

    # The code in this function is heavily modified from https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
    def fontHasSerif(self):
        if self.fontIndex >= len(fontNames):
            return
        filename = "n.png"
        src = cv.imread(filename, cv.IMREAD_GRAYSCALE)
        edges = cv.Canny(src, 50, 200, None, 3)
        grayscaleEdgesImg = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
        
        linesP = cv.HoughLinesP(edges, 1, math.pi, 25, None, 30, 10)
        
        if linesP is not None:
            for i in range(0, len(linesP)):
                l = linesP[i][0]
                cv.line(grayscaleEdgesImg, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
        else:
            # print("Handwriting", self.fontNames[self.fontIndex])
            return "Handwriting"

        sortlines = linesP
        sortlines = sortlines.tolist()

        minX, minY = sortlines[0][0][0], sortlines[0][0][1]
        otherY = sortlines[0][0][3]
        minIndex = 0
        for i in range(len(sortlines)):
            line = sortlines[i]
            x1, y1, x2, y2 = line[0][0], line[0][1], line[0][2], line[0][3]
            if x1 + y1 <= minX + minY:
                minX = x1
                minY = y1
                otherY = y2
                minIndex = i
            if x2 + y2 <= minX + minY:
                minX = x2
                minY = y2
                otherY = y1
                minIndex = i
                
        croppedEdges = edges[:, 0:minX]
        try:
            croppedImg = cv.cvtColor(croppedEdges, cv.COLOR_GRAY2BGR)
        except:
            croppedImg = grayscaleEdgesImg

        croppedLines = cv.HoughLinesP(croppedEdges, 1, math.pi/180, 10, None, 5, 10)
        
        if croppedLines is None:
            # print("Sans serif", self.fontNames[self.fontIndex])
            return "Sans serif"
        else:
            # print("Serif", self.fontNames[self.fontIndex])
            return "Serif"

    def redrawAll(self, canvas):
        canvas.create_text(self.width/2, self.width/2, text="N", font=(self.fontNames[self.fontIndex], 200))

        # canvas.create_rectangle(50, 100, 250, 500, fill='cyan')
        # if (self.image != None):
        #     canvas.create_image(525, 300, image=ImageTk.PhotoImage(self.image))
        #     

# AutoFontTagger(width=700, height=600)