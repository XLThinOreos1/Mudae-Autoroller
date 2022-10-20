import pyautogui
import time
import random
from pyautogui import *
import os

def ConsoleClear():
    os.system("cls")

print("Nico's Mudae auto roller v1.1")
print("-----------------------------")
print("Press ENTER to start")
input()

while True:
    ConsoleClear()

    print("What sort of roll are you using? (wa, wg, wx, ha, hg, hx, ma, mg, mx")
    sortofRoll = input()

    print("\nAre you using slash rolls? (Y/N)")
    slashRoll = input()

    print("\nAre you using stacked rolls? (us rolls) (Y/N)")
    usRollYesOrNo = input()

    # If user is using stacked rolls then don't ask for normal rolls
    if usRollYesOrNo == "N" or usRollYesOrNo == "n" or usRollYesOrNo == "no":
        print("\nHow many normal rolls do you have? TYPE NUMBERS ONLY")
        NormalRollsAmount = input()
    else:
        NormalRollsAmount = 0

    print("\nYou are using",sortofRoll)

    # Show user if they are using slash rolls or not
    if slashRoll == "Y" or slashRoll == "y" or slashRoll == "yes":
        print("\nYou are using slash rolls")
        slashRoll = True
        print(slashRoll)
    else:
        print("\nYou are not using slash rolls")
        slashRoll = False
        print(slashRoll)

    # Show user if they are using stacked rolls or not
    if usRollYesOrNo == "Y" or usRollYesOrNo == "y" or usRollYesOrNo == "yes":
        print("\nYou are using stacked rolls")
        usRollYesOrNo = True
        print(usRollYesOrNo)
    else:
        print("\nYou are not using stacked rolls")
        usRollYesOrNo = False
        print(usRollYesOrNo)

    # Show user how many normal rolls they have or if they are not using normal rolls
    if int(NormalRollsAmount) > 0:
        print("\nYou have", NormalRollsAmount, "rolls")
    else:
        print("\nYou are not using normal rolls and instead is using stacked rolls")

    print("\nIs this right? (Y/N)")
    SettingsCorrect = input()
    if SettingsCorrect == "y" or SettingsCorrect == "Y" or SettingsCorrect == "yes":
        break

ConsoleClear()

print("Waiting 2 seconds so you can focus the window to Discord...")
time.sleep(2)

ConsoleClear()

if slashRoll == True:
    while True:
        if usRollYesOrNo == True:
            print("Setting us 20...")
            keyDown("altright")
            press("4")
            keyUp("altright")
            pyautogui.typewrite("us 999999")
            pyautogui.press("enter")
            print("Done!")
            time.sleep(random.uniform(2.5, 3))
            for i in range(20):
                print("Rolling with us slash...")
                pyautogui.typewrite("/")
                pyautogui.typewrite(sortofRoll)
                time.sleep(3)
                pyautogui.press("enter")
                time.sleep(1)
                pyautogui.press("enter")
                print("Done!")
                time.sleep(random.uniform(2.5, 3))
        else:
            for i in range(int(NormalRollsAmount)):
                print("Rolling with normal slash...")
                pyautogui.typewrite("/")
                pyautogui.typewrite(sortofRoll)
                time.sleep(2)
                pyautogui.press("enter")
                time.sleep(1)
                pyautogui.press("enter")
                print("Done!")
                time.sleep(random.uniform(2.5, 3))
            print("No more rolls left!")
            break
else:
    while True:
        if usRollYesOrNo == True:
            print("Setting us 20 without slash command...")
            keyDown("altright")
            press("4")
            keyUp("altright")
            pyautogui.typewrite("us 999999")
            pyautogui.press("enter")
            print("Done!")
            time.sleep(random.uniform(2.5, 3))
            for i in range(20):
                print("Rolling with $",str(sortofRoll),"...")
                keyDown("altright")
                press("4")
                keyUp("altright")
                pyautogui.typewrite(sortofRoll)
                pyautogui.press("enter")
                print("Done!")
                time.sleep(random.uniform(2.5, 3))
        else:
            for i in range(int(NormalRollsAmount)):
                print("Rolling with normal rolls without slash...")
                keyDown("altright")
                press("4")
                keyUp("altright")
                pyautogui.typewrite(sortofRoll)
                pyautogui.press("enter")
                print("Done!")
                time.sleep(random.uniform(2.5, 3))
            print("No more rolls left!\nGoodbye!")
            break


# TODO: Implement Kakeraloot when the time is ready.
