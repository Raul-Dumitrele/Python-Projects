import pyautogui
import time
import os
import subprocess


pyautogui.FAILSAFE = True      # colțul stânga-sus oprește scriptul dacă e nevoie
pyautogui.PAUSE = 0.05         # mică pauză între acțiuni ca să fie stabil


# 1. Deschide Paint (merge pe Windows)
subprocess.Popen(["mspaint"])

# 2. Așteaptă să se încarce aplicația
time.sleep(0.5)

# 3. Maximiează fereastra (Alt+Space apoi X)
pyautogui.hotkey("alt", "space")
time.sleep(0.5)
pyautogui.press("x")
time.sleep(0.5)

# 4. Mută cursorul în mijlocul ecranului și dă click pentru a selecta zona de desen
screen_width, screen_height = pyautogui.size()
center_x, center_y = screen_width // 2, screen_height // 2
pyautogui.click(center_x, center_y)

# 5. Desenează spirala
distance = 250
while distance > 0:
    # right
    pyautogui.dragRel(distance, 0, duration=0.1)
    distance -= 5
    
    # down
    pyautogui.dragRel(0, distance, duration=0.1)
    distance -= 5
    
    # left
    pyautogui.dragRel(-distance, 0, duration=0.1)
    distance -= 5
    
    # up
    pyautogui.dragRel(0, -distance, duration=0.1)
    distance -= 5
