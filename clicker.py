import sys

import pyautogui
import win32gui, win32con
import time
import keyboard


# перемещение лаунчера
def logginInLauncher(hwnd, lParam):
    """Перемещатся лаунчер в левый верхний угол"""
    if win32gui.IsWindowVisible(hwnd):
        if 'Plarium Play' in win32gui.GetWindowText(hwnd):
            (win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE))
            time.sleep(1)
            (win32gui.ShowWindow(hwnd, True))
            win32gui.MoveWindow(hwnd, 0, 0, 760, 500, True)


# перемещение игры
def enumHandler(hwnd, lParam):
    """Перемещается окно с игрою в левый верхний угол"""
    if win32gui.IsWindowVisible(hwnd):
        if 'Raid: Shadow Legends' in win32gui.GetWindowText(hwnd):
            win32gui.MoveWindow(hwnd, 0, 0, 760, 500, True)


# контоль мыши в лаунчере
def controlMouseInLauncher(login, password):
    # выбор аккаунта
    time.sleep(2)
    pyautogui.click(235, 600)
    time.sleep(2)
    keyboard.write(login)
    pyautogui.click(530, 280)
    time.sleep(1)
    pyautogui.click(660, 345)
    # keyboard.press("enter")
    time.sleep(1)
    pyautogui.click(520, 310)

    # ПЕЧАТЬ ПАРОЛЯ
    keyboard.write(password)
    # keyboard.press("enter")
    time.sleep(1)
    pyautogui.click(660, 375)
    time.sleep(5)
    pyautogui.click(110, 245)
    time.sleep(3)
    pyautogui.click(950, 125)
    time.sleep(20)

# удаление акка
def delAccount():
    time.sleep(1)

    pyautogui.click(235, 600)
    time.sleep(1)
    pyautogui.click(125, 545)
    time.sleep(1)
    pyautogui.click(600, 380)
    time.sleep(2)
    pyautogui.click(630, 430)
    time.sleep(3)
    pyautogui.click(700, 250)
    time.sleep(3)
    pyautogui.click(600, 360)
    time.sleep(3)


# скип рекламы
def skipReklami():
    time.sleep(3)
    # скип рекламы
    pyautogui.click(745, 77)
    time.sleep(1)
    pyautogui.click(745, 77)
    time.sleep(1)
    pyautogui.click(745, 77)
    time.sleep(1)
    pyautogui.click(745, 77)
    time.sleep(1)
    pyautogui.click(745, 77)
    time.sleep(1)
    pyautogui.click(745, 77)
    time.sleep(1)
    pyautogui.click(745, 77)
    time.sleep(1)
    pyautogui.click(745, 77)
    time.sleep(1)
    pyautogui.click(18, 260)
    time.sleep(2)
    pyautogui.click(34, 70)
    time.sleep(2)
    time.sleep(1)


# забирает награды
def getErrdayBonus():
    # 1 СТРОКА
    # day 1
    pyautogui.click(350, 140)
    # day 2
    pyautogui.click(420, 140)
    # day 3
    pyautogui.click(490, 140)
    # day 4
    pyautogui.click(550, 140)
    # day 5
    pyautogui.click(625, 140)
    # day 6
    pyautogui.click(680, 140)
    # 2 СТРОКА
    # day 7
    pyautogui.click(350, 210)
    # day 8
    pyautogui.click(420, 210)
    # day 9
    pyautogui.click(490, 210)
    # day 10
    pyautogui.click(550, 210)
    # day 11
    pyautogui.click(625, 210)
    # day 12
    pyautogui.click(680, 210)
    # 3 СТРОКА
    # day 13
    pyautogui.click(350, 280)
    # day 14
    pyautogui.click(420, 280)
    # day 15
    pyautogui.click(490, 280)
    # day 16
    pyautogui.click(550, 280)
    # day 17
    pyautogui.click(625, 280)
    # day 18
    pyautogui.click(680, 280)
    # 4 СТРОКА
    # day 19
    pyautogui.click(350, 350)
    # day 20
    pyautogui.click(420, 350)
    # day 21
    pyautogui.click(490, 350)
    # day 22
    pyautogui.click(550, 350)
    # day 23
    pyautogui.click(625, 350)
    # day 24
    pyautogui.click(680, 350)
    # 5 СТРОКА
    # day 25
    pyautogui.click(350, 420)
    # day 26
    pyautogui.click(420, 420)
    # day 27
    pyautogui.click(490, 420)
    # day 28
    pyautogui.click(550, 420)
    # day 29
    pyautogui.click(625, 420)
    # day 30
    pyautogui.click(680, 420)


# выход из игры
def exitInGame():
    # нажатие крестика
    time.sleep(2)
    pyautogui.click(729, 13)

    # согласиться закрыть
    time.sleep(2)
    pyautogui.click(460, 285)

    time.sleep(3)






def main():
    # readFile()
    fileName = open("plarium.txt", encoding='cp1251')
    data = fileName.readlines()
    for i in data:
            # if keyboard.is_pressed('q'):
            #     sys.exit()
            

        password, login = i.strip().split(" login: ")

        win32gui.EnumWindows(logginInLauncher, None)  # перемещение лаунчера в верхний левый угол
        controlMouseInLauncher(login, password)  # контроль мыши запуск игры
        win32gui.EnumWindows(enumHandler, None)  # перемещение игры в левый верхний угол
        skipReklami()  # скип рекламы
        getErrdayBonus()  # забирает ежедневную награду
        exitInGame()  # выходит из игры
        time.sleep(1)
        pyautogui.click(760, 143)
        time.sleep(1)
        delAccount()




if keyboard.is_pressed('z'):
    sys.exit()
else:
    main()

#
# if __name__ == "__main__":
#     main()




