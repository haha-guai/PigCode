import pyautogui as pg
import time



position_color = (1639, 532)
position_replace = (1673, 709)
position_forget = (1457, 711)
position_find = (1584, 710)
color = (222, 104, 78)

while 1:
    pg.click(position_find)
    if pg.pixelMatchesColor(1489, 501, color):
        pg.click(x=1489, y=501)
        pg.click(position_replace)
    else:
        pg.click(position_forget)
    time.sleep(2)

