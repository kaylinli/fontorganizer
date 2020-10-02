# by Bhavesh Mevada https://stackoverflow.com/questions/54832003/how-to-retrieve-actual-font-file-name-in-python
import os
from cmu_112_graphics import *

list = []
for file in os.listdir(r'C:\Windows\Fonts'):
    if file.endswith(".ttf"):
        list.append(file)

print(list)

def redrawAll(app, canvas):
    count = 0
    for file in list:
        try:
            canvas.create_text(app.width/2, count, text=f'{file}')
        except:
            print(f'{file}')
        count +=20

runApp(width = 500, height = 500)