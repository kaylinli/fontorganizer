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
    self.widgets = [] # list of widgets
    self.selectedWidget = 0
    self.widgetText = []
    self.widgetText +=["hello"]
    pass

'''
Controller
'''
def mousePressed(self, event):
    pass

'''
View
'''

def drawWidgets(self, canvas):
    width = random.randrange(100,200)
    height = random.randrange(100,200)
    drawTextWidget(self, canvas, 0, self.marginLeft, 80, self.marginLeft + width, 80 + height)

def drawTextWidget(self, canvas, widgetNum, x0, y0, x1, y1):
    canvas.create_rectangle(x0, y0, x1, y1)
    canvas.create_text((x0+x1)/2, (y0+y1)/2, text=self.widgetText[widgetNum])
    

def createHeader(self, canvas):
    canvas.create_text(self.marginLeft, 30, text="font explorer", anchor="w", font=("Red Hat Display Medium", 24))


def drawFontExplorerUI(self, canvas):
    createHeader(self, canvas)
    drawWidgets(self, canvas)
