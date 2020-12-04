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
def checkIfClickedButton(clickx, clicky, boundx, boundy, width, height):
    if (boundx - width/2 < clickx < boundx + width/2) and \
        (boundy - height/2 < clicky < boundy + height/2):
        return True
    else:
        return False