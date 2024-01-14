"""
ADD A DOCSTRING
"""
import time
import cv2
import pyautogui
from PIL import ImageGrab
import numpy as np


def take_screenshot(coordinates):
    # Take + save screenshot
    time.sleep(5)
    ImageGrab.grab(coordinates).save('../images/gpt_screenshot.png')


def match_images():
    screenshot_cur = cv2.imread('../images/gpt_screenshot.png')
    gray_screenshot_cur = cv2.cvtColor(screenshot_cur, cv2.COLOR_BGR2GRAY)

    screenshot_copy = cv2.imread('../images/copy_code.png')
    gray_screenshot_copy = cv2.cvtColor(screenshot_copy, cv2.COLOR_BGR2GRAY)

    # Match the icon in the screenshot
    result = cv2.matchTemplate(gray_screenshot_cur, gray_screenshot_copy, cv2.TM_CCOEFF_NORMED)

    # Set a threshold
    threshold = 0.5
    # Get the locations of the icon in the screenshot
    locations = np.where(result >= threshold)

    pyautogui.click(locations[1][0] + 10, locations[0][0] + 5)
    time.sleep(2)
    pyautogui.moveTo(1109, 899)
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.hotkey('command', 'v')

    return locations[1][0], locations[0][0]


def match_images2():
    img_rgb = cv2.imread('../images/gpt_screenshot.png')
    template = cv2.imread('../images/copy_code.png')
    w, h = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .5
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  # Switch columns and rows
        cv2.rectangle(img_rgb, pt, (pt[0] + h, pt[1] + w), (0, 0, 255), 2)
        print(pt)

    cv2.imwrite('result.png', img_rgb)


def transfer_data():
    coord = (485, 135, 1120, 810)
    coord = (0, 0, 1439, 899)
    # coord = (1002, 530, 1079, 546,)
    take_screenshot(coord)
    time.sleep(2)
    # match_images2()
    match_images()


def main():
    transfer_data()


if __name__ == "__main__":
    main()
