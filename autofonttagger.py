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
print(fontNames)
win32gui.ReleaseDC(hdc, None)
# above code from https://stackoverflow.com/questions/51256688/python-windows-enum-installed-fonts

from cmu_112_graphics import *

class MyApp(App):
    def appStarted(self):
        self.image = None
        self.hasSerif = False

    def keyPressed(self, event):
        if (event.key == 'g'):
            snapshotImage = self.getSnapshot()
            self.saveSnapshot("n.png")
            self.fontHasSerif()
            # self.image = self.scaleImage(snapshotImage, 0.4)
            
    
    def fontHasSerif(self):
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
            print("Sans serif and none")
            return "Sans serif"
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

        croppedImg = cv.cvtColor(croppedEdges, cv.COLOR_GRAY2BGR)

        croppedLines = cv.HoughLinesP(croppedEdges, 1, math.pi/180, 10, None, 5, 10)
        
        if croppedLines is None:
            print("Sans serif")
            return "Sans serif"
        else:
            print("Serif")
            return "Serif"

    def redrawAll(self, canvas):
        canvas.create_text(525, 300, text="N", font=("Zilla Slab", 100))

        # canvas.create_rectangle(50, 100, 250, 500, fill='cyan')
        # if (self.image != None):
        #     canvas.create_image(525, 300, image=ImageTk.PhotoImage(self.image))
        #     

MyApp(width=700, height=600)