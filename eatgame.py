
import pgzrun
import random
 
WIDTH = 800
HEIGHT = 600
alien_hurt = Actor('alien', midbottom=(WIDTH // 2, HEIGHT))
alien = Actor('alien_hurt')
alien.topright = 100, 10
 
 
def draw():
    screen.fill('black')
    alien.draw()
    alien_hurt.draw()
 
 
xpos = random.randint(0, 800) 
ypos = random.randint(0, 600) 
 
def update():
    global xpos
    global ypos
    alien.y += 5
    if keyboard.left:
        alien.x -= 5
    if keyboard.right:
        alien.x += 5
    if alien_hurt.colliderect(alien):
        print('you win')
        alien.y = 0
        xpos = random.randint(0, 800)
        ypos = random.randint(0, 600)
        alien.x = xpos
        alien.y = ypos
    if alien.y > 600:
        print("you lose")
        alien. y = 0
        xpos = random.randint(0, 800)
        ypos = random.randint(0, 600)
        alien.x = xpos
        alien.y = ypos
    if keyboard.up:
        alien.y -= 2
    if keyboard.down:
        alien.y += 5


pgzrun.go()
