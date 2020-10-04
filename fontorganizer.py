import os
# from cmu_112_graphics import *

list = []
for file in os.listdir(r'C:\Windows\Fonts'):
    if file.endswith(".ttf"):
        list.append(file)
    if file.endswith(".otf"):
        list.append(file)

# above is modified code from Bhavesh Mevada's StackOverflow post
# https://stackoverflow.com/questions/54832003/how-to-retrieve-actual-font-file-name-in-python

import tkinter as tk

fontEntries = 20
totalPages = len(list) // fontEntries
entries = []

class Page(tk.Frame):
    def __init__(self, title):
        tk.Frame.__init__(self, bd=1, relief="sunken")
        self.labels = []
        rowNum = 0
        for field in title:
            try:
                rowNum += 1
                fontType = str(field)
                fontType = fontType[:(len(fontType)-4)]
                fontType.replace(" ", "_")
                self.label = tk.Label(self, text=fontType, font=fontType, anchor='w')
                # self.label = tk.Label(row, width=15, text=field, anchor='w')
                # self.label.pack()
                self.label.grid(row=rowNum, column=1)
                self.labels.append(self.label)
                self.ent = tk.Entry(self)
                self.ent.grid(row=rowNum, column=2)
                # self.ent.pack()
                # entries.append((fontType, self.ent))
            except Exception as e:
                print(e)
                print(field)
        # self.label.pack()

    def show(self):
        self.lift()

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)

        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        nextButton = tk.Button(buttonframe, text=" > ", command=self.nextPage)
        prevButton = tk.Button(buttonframe, text=" < ", command=self.prevPage)
        saveButton = tk.Button(buttonframe, text=" Save tags ", command=self.saveTags)
        prevButton.pack(side="left")
        nextButton.pack(side="left")
        saveButton.pack(side="left")


        self.pages = []
        fields = getFields()
        totalPages = getTotalPages(root)
        fontEntries = getFontEntries(root)
        for pageNum in range(totalPages):
            firstEntry = pageNum * fontEntries
            currentFields = fields[firstEntry:(firstEntry+fontEntries)]
            page = Page(title=currentFields)
            page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            self.pages.append(page)

        self.pages[0].show()

    def nextPage(self):
        # move the first page to the end of the list, 
        # then show the first page in the list
        page = self.pages.pop(0)
        self.pages.append(page)
        self.pages[0].show()

    def prevPage(self):
        # move the last page in the list to the front of the list,
        # then show the first page in the list.
        page = self.pages.pop(-1)
        self.pages.insert(0, page)
        self.pages[0].show()

    def saveTags(self):
        for entry in entries:
            field = entry[0]
            text  = entry[1].get()
            if text != "":
                print('%s: "%s"' % (field, text))

# def fetch(entries):
#     for entry in entries:
#         field = entry[0]
#         text  = entry[1].get()
#         print('%s: "%s"' % (field, text)) 

def getFields():
    return list

def getFontEntries(root):
    fontEntries = root.winfo_height() // 40
    if fontEntries == 0:
        fontEntries = 15
    return fontEntries

def getTotalPages(root):
    totalPages = len(list) // getFontEntries(root)
    return totalPages

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    # ents = makeform(root, list)
    # root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()

#https://stackoverflow.com/questions/47562800/tkinter-navigate-through-pages-with-button
