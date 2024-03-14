import curses
import random

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

maxl = curses.LINES - 1
maxc = curses.COLS - 1

world = []
plyayer_l = plyayer_c = 0
def init():
    global plyayer_c, plyayer_l
    for i in range(maxl):
        world.append([])
        for j in range(maxc):
            world[i].append(' ' if random.random() > 0.03 else '.')
    plyayer_l = random.randint(0, maxl)
    plyayer_c = random.randint(0, maxc)




def draw():
    for i in range(maxl):
        for j in range(maxc):
            stdscr.addch(i, j, world[i][j])
    stdscr.addch(plyayer_l, plyayer_c, 'x')    
    stdscr.refresh()

def move(c):
    ''' get one of asdw and moved towrad that direction'''
    pass

init()

playgin = True
while playgin:
    c = stdscr.getkey()
    if c ["asdw"]:
        move(c)
    elif c == 'q':
        playding = False
    draw()  

