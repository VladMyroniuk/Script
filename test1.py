import pyautogui as pg
import keyboard as k
import time as t

p1 = int(input('p1'))   # start pos
p2 = int(input('p2'))   # end pos
an = input('an')        # account nummer
rn = input("rn")        # roating nummer
login = input("login")  # login
password = input("pass")# pass
global j
j = 0
while p2 + 1 >= p1:
    t.sleep(0.05)
    cp1 = str(p1)
    while True:
        if k.is_pressed("="):
            k.press("backspace")
            if k.is_pressed("a") and j == 0:
                k.press("backspace")
                pg.write(cp1 + an)
                p1 += 1
                if p2 < p1:
                    j = 1
                break
            if k.is_pressed("a") and j == 1:
                break
            elif k.is_pressed("r"):
                k.press("backspace")
                pg.write(rn)
                break
            elif k.is_pressed("l"):
                k.press("backspace")
                pg.write(login)
                break
            elif k.is_pressed("p"):
                k.press("backspace")
                pg.write(password)
                break
            elif k.is_pressed("s"):
                print(p1)
                print("Program stopped)")
                p1 = p2 + 2
                break
            else:
                break
