import os
from cmu_112_graphics import *

list = []
for file in os.listdir(r'C:\Windows\Fonts'):
    if file.endswith(".ttf"):
        list.append(file)
    if file.endswith(".otf"):
        list.append(file)

# above is code by Bhavesh Mevada, modified slightly
# https://stackoverflow.com/questions/54832003/how-to-retrieve-actual-font-file-name-in-python

print(list)

def appStarted(app):
    app.entryHeight = 20
    app.fontEntries = app.width//20 - 2# number of entries on a page
    app.pageNum = 0
    app.forwardButtonX = app.width/2 + 20
    app.forwardButtonY = app.height - 10
    app.backButtonX = app.width/2 - 20
    app.backButtonY = app.height - 10

def mousePressed(app, event):
    if app.forwardButtonX-20 < event.x < app.forwardButtonX+20:
        app.pageNum += 1
    if app.backButtonX-20 < event.x < app.backButtonX+20:
        if app.pageNum != 0:
            app.pageNum -= 1

def pageSetup(app, canvas):
    count = app.entryHeight
    firstEntry = app.pageNum * app.fontEntries
    for file in list[firstEntry:(firstEntry+app.fontEntries)]:
        try:
            fontType = str(file)
            fontType = fontType[:(len(fontType)-4)]
            fontType.replace(" ", "_")
            canvas.create_text(10, count, anchor='w', text=f'{file}', font=fontType)
        except Exception as e:
            print(e)
            print(fontType)
        count += app.entryHeight
    
def redrawAll(app, canvas):
    pageSetup(app, canvas)
    canvas.create_rectangle(app.forwardButtonX-10, app.forwardButtonY-10, app.forwardButtonX+10,app.forwardButtonY+10)
    canvas.create_rectangle(app.backButtonX-10, app.backButtonY-10, app.backButtonX+10,app.backButtonY+10)
    canvas.create_text(app.forwardButtonX, app.forwardButtonY, text='>')
    canvas.create_text(app.backButtonX, app.backButtonY, text='<')
    

runApp(width = 500, height = 500)