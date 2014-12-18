__author__ = 'dugging'
from Engine import *
from tkinter import *

map1 = Map(4, 4)
map1.creategrid(map1.width, map1.height)
for x in range(map1.width):
    for y in range(map1.height):
        map1.map[x][0] = 'W'
        map1.map[x][map1.height-1] = 'W'
        map1.map[0][y] = 'W'
        map1.map[map1.width-1][y] = 'W'
        #map1.map[1][1] = 'F'
        #map1.map[1][2] = 'F'
        #map1.map[2][1] = 'F'
        #map1.map[2][2] = 'F'
print(map1.map)


def window(MAP):
    GUI = Tk()
    for x in range(len(MAP.map)):
        for y in range(len(MAP.map[x])):
            Label(GUI, text=str(MAP.map[x][y])).grid(column=x, row=y)
    GUI.mainloop()

window(map1)