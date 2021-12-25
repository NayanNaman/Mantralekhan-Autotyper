#we did the funniest thing in the world XD

#imports
import pyautogui, time, webbrowser

#input
print ("\nEnter 0 for typing unlimited times.")
x = int(input("\nEnter the number of times you want to type: "))
print ("\nSwitch to the window you want to type in.")

#main_code
i = 0
time.sleep(5)

#webbrowser.open("mantralekhan.com")
#you can also enable webbrowser function

while i < x or i == 0:
    f = "swaminarayan"
    for words in f:
        pyautogui.typewrite(words)
    if x > 0 :
        i = i + 1
    elif x == 0:
        i = i - 1
print ("\nDONE!")

