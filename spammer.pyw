import pyautogui
import sys
import time


def main():
    start_spam()

def start_spam():
    toSpam = "You message goes here"
    no_spam = 30
    time.sleep(5)
    for i in range(no_spam):
        pyautogui.click(button='left')
        pyautogui.typewrite(toSpam, interval=0)
        pyautogui.press('enter')
    print("Spammed Succesfully")
    sys.exit()
main()
