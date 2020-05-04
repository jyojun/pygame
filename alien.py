import pgzrun
import time

alien = Actor('alien')
#alien.pos = 100, 56
alien.topright = 0, 10

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

score = 0

def on_mouse_down(pos):
    global score
    if alien.collidepoint(pos):
        set_alien_hurt()
        score += 1
    else:
        score -= 1
        print("Nothing here")
    print(score)


def set_alien_hurt():
    alien.image = 'alien_hurt'
    #sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 0.5)


def set_alien_normal():
    alien.image = 'alien'


pgzrun.go()
