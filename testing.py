__author__ = 'dugging'
from Engine import *
from tkinter import *

map1 = Map(14, 20)
map1.creategrid(map1.width, map1.height)
for x in range(map1.width):
    for y in range(map1.height):
        map1.map[x][0] = 'W'
        map1.map[x][map1.height-1] = 'W'
        map1.map[0][y] = 'W'
        map1.map[map1.width-1][y] = 'W'
map1.map[7][3] = 'P'


map1.fillfloor()
#print(map1.map)
IO = IOData()
IO.save('', 'map1', '.txt', map1)
map2 = IO.load('', 'map1', '.txt')
IO.save('', 'map1', '.txt', map2=
map3 = IO.load('', 'map1', '.txt')

def window(MAP):
    GUI = Tk()
    for x in range(len(MAP.map)):
        for y in range(len(MAP.map[x])):
            Label(GUI, text=str(MAP.map[x][y])).grid(column=x, row=y)
    GUI.mainloop()

window(map3)