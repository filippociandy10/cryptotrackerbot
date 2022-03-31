
import cv2
import time
template = cv2.imread("Template/template.png")
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", template)
cv2.waitKey(0)
