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
        print("event.key",event.key)
        text += event.key
    return text

def checkIfClickedButton(clickx, clicky, boundx, boundy, width, height):
    if (boundx - width/2 < clickx < boundx + width/2) and \
        (boundy - height/2 < clicky < boundy + height/2):
        return True
    else:
        return False

def saveTagsToComputer(self):
    file = open("fonttags.txt", "w")
    print("hello")
    for font in self.app.fontTags:
        file.write(f"{font}: ")
        for i in range(len(self.app.fontTags[font])):
            tag = self.app.fontTags[font][i]
            if i == len(self.app.fontTags[font])-1:
                file.write(f"{tag}")
            else:
                file.write(f"{tag}, ")
        file.write("\n")


