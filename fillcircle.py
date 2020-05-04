import pgzrun

#two colors and the default background color
RED = 150, 0, 0
GREEN = 0, 128, 0
bg = RED

#screen size
WIDTH = 800
HEIGHT = 600

def draw(): #this draws a circle on the screen
    screen.fill(bg)
    screen.draw.circle((400,300), 30, (255,255,255,))


def on_mouse_down(): #when you click the mouse
    global bg
    bg = GREEN

def on_mouse_up(): #when you release the mouse
    global bg
    bg = RED

pgzrun.go()
