import subprocess
import pyautogui
import time


def open_app():
    # open app
    subprocess.Popen(['C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE'])
    time.sleep(3)

    # search Campus
    pyautogui.keyDown("F3")
    pyautogui.write("campus")
    time.sleep(3)
    pyautogui.keyDown("Enter")
    time.sleep(5)

    # move to unread
    # bydate = pyautogui.locateCenterOnScreen("bydate.png")
    # pyautogui.moveTo(bydate)
    # pyautogui.click()
    # time.sleep(2)
    # unread = pyautogui.locateCenterOnScreen("unread.png")
    # pyautogui.moveTo(unread)
    # pyautogui.click()
    # time.sleep(2)

    # click on email
    pyautogui.moveTo(300,200)
    pyautogui.click()
    time.sleep(2)

    # click on link
    link = pyautogui.locateCenterOnScreen("link.png")
    pyautogui.moveTo(link)
    pyautogui.click()
    time.sleep(5)

    # enter sapid and join

    sap = pyautogui.locateOnScreen("sapidinput.png")
    pyautogui.moveTo(sap)
    pyautogui.click()
    pyautogui.write("70612000057")
    robotcheck = pyautogui.locateOnScreen("robotcheck.png")
    pyautogui.moveTo(robotcheck)
    pyautogui.click()
    joinmeeting = pyautogui.locateOnScreen("joinmeeting.png")
    pyautogui.moveTo(joinmeeting)
    pyautogui.click()
    time.sleep(2)
    openzoom = pyautogui.locateOnScreen("openzoommeet.png")
    pyautogui.moveTo(openzoom)
    pyautogui.click()


open_app()
