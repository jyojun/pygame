import pgzrun
from random import randint
 
WIDTH = 800
HEIGHT = 600
alien_hurt = Actor('alien', midbottom=(WIDTH // 2, HEIGHT))
alien = Actor('alien_hurt')
alien.topright = 100, 10
xpos = randint(0, 800)
score = 0
lor = randint(0, 1)
somewhere = randint(0, 0)
 
 
def draw():
    screen.fill('black')
    alien.draw()
    alien_hurt.draw()
 
 
def update():
    global score, somewhere
    alien.y += 5 + somewhere
    alien.x += somewhere
    if alien_hurt.x > 30:
        if keyboard.left:
            alien_hurt.x -= 10
    if alien_hurt.x < 770:
        if keyboard.right:
            alien_hurt.x += 10
    if alien_hurt.colliderect(alien):
        score += 1
        respawn()
    if alien.y > 600:
        score -= 1
        respawn()
    if alien.x < 30 or alien.x > 770:
        somewhere = -somewhere
 
 
def respawn():
    global somewhere
    print(score)
    alien.y = 0
    xpos = randint(0, 800)
    alien.x = xpos
    somewhere = randint(-3, 3)
 
pgzrun.go()
