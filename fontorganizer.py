import os
# from cmu_112_graphics import *

list = []
for file in os.listdir(r'C:\Windows\Fonts'):
    if file.endswith(".ttf"):
        list.append(file)
    if file.endswith(".otf"):
        list.append(file)

# above is code by Bhavesh Mevada, modified slightly
# https://stackoverflow.com/questions/54832003/how-to-retrieve-actual-font-file-name-in-python

import tkinter as tk

fields = list

pageNum = 0
fontEntries = 20

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text)) 

def changePages(boolean,pageNum):
    # boolean == 0 means clicked back a page
    # boolean == 1 means clicked forward a page
    if boolean == 0 and pageNum != 0:
        pageNum -= 1
    if boolean == 1:
        pageNum += 1

def makeform(root, fields):
    entries = []
    firstEntry = pageNum * fontEntries
    for field in fields[firstEntry:(firstEntry+fontEntries)]:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    # b1 = tk.Button(root, text='Show',
    #               command=(lambda e=ents: fetch(e)))
    # b2 = tk.Button(root, text='Quit', command=root.quit)
    b1 = tk.Button(root, text='<', command=(lambda e=ents: changePages(0,pageNum)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='>', command=(lambda e=ents: changePages(1,pageNum)))
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()

# above code modified from python course
# https://www.python-course.eu/tkinter_entry_widgets.php
