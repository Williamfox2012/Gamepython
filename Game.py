import curses
stdscr = curses.initscr()

maxl = curses.LINES - 1
maxc = curses.COLS - 1


world = []

def init():
    for i in range(maxl):
        world[i] = []
        for j in range(maxc):
            world[i][j] = '.'

def draw():
    for i in range(maxl):
        for j in range(maxc):
            stdscr.addch(i, j, world[i][j])

curses.noecho()
curses.cbreak()
stdscr.keypad(True)



stdscr.refresh()
stdscr.getkey()