"""
@file hough_lines.py
@brief This program demonstrates line finding with the Hough transform
"""
import sys
import math
import cv2 as cv
import numpy as np
def main(argv):
    
    filename = 'serifn.jpg'

    src = cv.imread(filename, cv.IMREAD_GRAYSCALE)
    print(src[0][0])
    print(type(src))
    print("height src", len(src))
    print("width src", len(src[0]))

    edges = cv.Canny(src, 50, 200, None, 3)

    # print(len(dst))
    # print(type(dst))
    # print("height dst", len(dst))
    # print("width dst", len(dst[0]))
    
    grayscaleEdgesImg = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
    
    linesP = cv.HoughLinesP(edges, 1, math.pi, 25, None, 30, 10)
    # print(linesP)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(grayscaleEdgesImg, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
     
    #trying to find top left most line to identify serif
    # print(linesP)
    sortlines = linesP
    sortlines = sortlines.tolist()
    # print(sortlines)
    minX, minY = sortlines[0][0][0], sortlines[0][0][1]
    otherY = sortlines[0][0][3]
    minIndex = 0
    for i in range(len(sortlines)):
        line = sortlines[i]
        x1, y1, x2, y2 = line[0][0], line[0][1], line[0][2], line[0][3]
        if x1 <= minX and y1 <= minY:
            minX = x1
            minY = y1
            otherY = y2
            minIndex = i
        if x2 <= minX and y2 <= minY:
            minX = x2
            minY = y2
            otherY = y1
            minIndex = i
    
    print(minX, line[0][i])

    # print(dst)
    croppedEdges = edges[:, 0:minX]
    # print(croppedArea)

    croppedImg = cv.cvtColor(croppedEdges, cv.COLOR_GRAY2BGR)

    croppedLines = cv.HoughLinesP(croppedEdges, 1, math.pi/180, 10, None, 5, 10)
    print(croppedLines)
    if croppedLines is None:
        print("Sans serif")
    else:
        print("Serif")

    if croppedLines is not None:
        for i in range(0, len(croppedLines)):
            l = croppedLines[i][0]
            cv.line(croppedImg, (l[0], l[1]), (l[2], l[3]), (0,0,255), 1, cv.LINE_AA)
    

    # this code tells us that there are two values in the grayscale image
    # 255 = white, 0 = black 
    sortpoints = edges.flatten()
    # sortpoints = np.sort(sortpoints)
    sortpoints = np.unique(sortpoints)
    # print(sortpoints)


    cv.circle(grayscaleEdgesImg,(minX, minY),5,(0, 0, 255),-1,8)
    
    # cv.imshow("Source", src)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", grayscaleEdgesImg)
    cv.imshow("Cropped Area", croppedImg)
    
    cv.waitKey()
    cv.destroyAllWindows()
    return 0
    
if __name__ == "__main__":
    main(sys.argv[1:])

# adapted from https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
# Noah image source: https://unblast.com/noah-sans-serif-font/
# Solomon image source: https://creativetacos.com/solomon-serif-font-family/


'''
Random scrap code
'''
    # sortpoints = src
    # sortpoints.astype(set)
    # string = ""
    # for value in sortpoints:
    #     string += f"{value}"
    # print("string")
    # print(string)

    # print("sorted point", sortpoints[0][0])
    # print("sorted point", sortpoints[len(sortpoints)-1][len(sortpoints[0])-1])