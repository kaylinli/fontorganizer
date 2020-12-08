'''
This code is written by Kaylin Li. 
All code not written by Kaylin is credited next to the corresponding section.
'''

# def checkIfClickedButton(x, y, xbound0, ybound0, xbound1, ybound1):
#     if xbound0 < x < xbound1 and ybound0 < y < ybound1:
#         return True
#     else:
#         return False

# note: boundx and boundy should be cxs and cys
def checkForInput(self, event, text):
    if event.key == "Backspace":
        text = text[:len(text)-1]
    elif event.key == "Space":
        text += " "
    else:
        text += event.key
    return text

def checkIfClickedButton(clickx, clicky, boundx, boundy, width, height):
    if (boundx - width/2 < clickx < boundx + width/2) and \
        (boundy - height/2 < clicky < boundy + height/2):
        return True
    else:
        return False

def drawButton(self, canvas, coords, width, height, buttonText):
        x0, x1 = coords[0] - width/2, coords[0] + width/2
        y0, y1 = coords[1] - height/2, coords[1] + height/2
        canvas.create_rectangle(x0, y0, x1, y1)
        canvas.create_text(coords[0], coords[1], text=buttonText)

def saveTagsToComputer(self):
    file = open("fonttags.txt", "w")
    for font in self.app.fontTags:
        file.write(f"{font}: ")
        for i in range(len(self.app.fontTags[font])):
            tag = self.app.fontTags[font][i]
            if i == len(self.app.fontTags[font])-1:
                file.write(f"{tag}")
            else:
                file.write(f"{tag}, ")
        file.write("\n")


