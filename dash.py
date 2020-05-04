import pgzrun
import pygame
import random

pygame.init()

win = pygame.display.set_mode((1000, 250))

pygame.display.set_caption("Dash")

#Put colors here
black = (0,0,0)
green = (0,255,0)
white = (255, 255, 255)
purple = (255, 0, 255)

bottom = pygame.draw.rect(win, green, (0 , 245, 1000, 5))

class Dash(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25,25])
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.score = 0
    def draw(self):
        win.blit(self.image, (self.rect.x,self.rect.y))

class BottomPipes(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25,100])
        self.image.fill(purple)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x -= 10 + dash.score // 10
        if self.rect.x < 0:
           self.rect.x = random.randint(950,1000)
           self.rect.y = random.randint(200,240)
           self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
           dash.score += 1

class Star(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2,2])
        self.image.fill(white)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x -= 10 + dash.score // 10
        if self.rect.x < 0:
            self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.rect.x = random.randint(500,1500)
            self.rect.y = random.randint(0,240)



#Call classes to create objects
dash = Dash()
dash.rect.x = 250
dash.rect.y = 225

Bpipes = BottomPipes()
Bpipes.rect.x = 700
Bpipes.rect.y = 225

B2pipes = BottomPipes()
B2pipes.rect.x = 400
B2pipes.rect.y = 225

B3pipes = BottomPipes()
B3pipes.rect.x = 1000
B3pipes.rect.y = 225

star_list = pygame.sprite.Group()
for i in range(100):
    star = Star()
    star.rect.x = random.randint(0,1000)
    star.rect.y = random.randint(0,240)
    star.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    star_list.add(star)

pipes_list = pygame.sprite.Group()
pipes_list.add(Bpipes, B2pipes, B3pipes)

def redraw():
    win.fill((0,0,0))
    star_list.draw(win)
    star_list.update()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render(str(dash.score), False, white)
    textRect = text.get_rect()
    win.blit(text, textRect)
    dash.draw()
    pipes_list.draw(win)
    pipes_list.update()
    bottom = pygame.draw.rect(win, green, (0 , 245, 1000, 5))
    pygame.display.update()

run = True

while run:

    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and dash.rect.y >= 215:
        while dash.rect.y > 100:
            dash.rect.y += -1
    if key[pygame.K_RIGHT]:
        dash.rect.x += 5

    if key[pygame.K_LEFT]:
        dash.rect.x -= 5

    if not dash.rect.colliderect(bottom):
        dash.rect.y += 5 + dash.score//10
    

    for thing in pipes_list:
        if thing.rect.colliderect(dash.rect):
            dash.score -= 1

    redraw()

pygame.quit()
pgzrun.go()
