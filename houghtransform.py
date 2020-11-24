"""
@file hough_lines.py
@brief This program demonstrates line finding with the Hough transform
"""
import sys
import math
import cv2 as cv
def main(argv):
    
    filename = 'solomon.jpg'

    src = cv.imread(filename, cv.IMREAD_GRAYSCALE)

    dst = cv.Canny(src, 50, 200, None, 3)
    
    cdstP = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    
    linesP = cv.HoughLinesP(dst, 1, math.pi/90, 25, None, 30, 10)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
    
    cv.imshow("Source", src)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
    
    cv.waitKey()
    return 0
    
if __name__ == "__main__":
    main(sys.argv[1:])

# adapted from https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
# Noah image source: https://unblast.com/noah-sans-serif-font/
# Solomon image source: https://creativetacos.com/solomon-serif-font-family/