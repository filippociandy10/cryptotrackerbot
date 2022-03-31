from screenshot import screenshot, openscreen
from detect import determine
from bot import algorithm
import cv2


def main():
    url = "https://www.youtube.com/watch?v=jJNV2anmw6A&ab_channel=RaishizCrypto"
    im2 = cv2.imread("pictures/screenshot.png")
    openscreen(url)
    indicator_before = "NULL"
    max_x_before = 0
    while True:
        screenshot()
        algorithm(max_x_before, indicator_before, im2)
        indicator_before, max_x_before = determine(im2)


main()
