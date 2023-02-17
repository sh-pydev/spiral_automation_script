import pyautogui as pg
import time as t

t.sleep(3)
pg.leftClick(839,1045,2)
pg.press(['p','a','i','n','t'])
pg.press('enter')
t.sleep(5)
pg.leftClick(1655,121)
t.sleep(3)
pg.moveTo(641,336)
distance = 600
while distance>0:
  pg.dragRel(distance,0,0)
  pg.dragRel(0,distance,0)
  distance -= 20
  pg.dragRel(-distance,0,0)
  pg.dragRel(0,-distance,0)
  distance -= 20
