import pygame
import sys

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

#iconChoice = input("Would you like to be X's or O's?(X/O)?:")

iconChoice = "X"

# initialize game engine
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Century Schoolbook",12)
# set screen width/height and caption
size = [500,500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

# Loop until the user clicks close button
done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # write game logic here

    sys_font = pygame.font.SysFont("None",60)
    rendered = sys_font.render(iconChoice, 0, black)
    mousexpos, mouseypos = pygame.mouse.get_pos()
    pygame.event.get()


    if pygame.mouse.get_pressed()[0] == True and mousexpos > 166 and mousexpos < 322 and  mouseypos < 156:
        print("2")

    elif pygame.mouse.get_pressed()[0] == True and mousexpos > 332 and  mouseypos < 156:
        print("3")
        done = True

    elif pygame.mouse.get_pressed()[0] == True and mousexpos < 156 and  mouseypos > 166 and mouseypos < 322:
        print("4")
        done= True

    elif pygame.mouse.get_pressed()[0] == True and mousexpos > 166 and mousexpos < 322 and  mouseypos > 166 and mouseypos < 322:
        print("5")
        done= True

    elif pygame.mouse.get_pressed()[0] == True and mousexpos > 332 and  mouseypos > 166 and mouseypos < 322:
        print("6")
        done = True

    elif pygame.mouse.get_pressed()[0] == True and mousexpos < 156 and  mouseypos > 332:
        print("7")
        done= True

    elif pygame.mouse.get_pressed()[0] == True and mousexpos > 166 and mousexpos < 322 and  mouseypos > 332:
        print("8")
        done= True

    elif pygame.mouse.get_pressed()[0] == True and mousexpos > 332 and  mouseypos > 332:
        print("9")
        done = True



    # clear the screen before drawing
    screen.fill((255, 255, 255))


    # draw
    pygame.draw.rect(screen, black, (10,156,480,15), 0)
    pygame.draw.rect(screen, black, (10,322,480,15), 0)
    pygame.draw.rect(screen, black, (156,10,15,480), 0)
    pygame.draw.rect(screen, black, (322,10,15,480), 0)
    pygame.display.flip()

    if pygame.mouse.get_pressed()[0] == True and mousexpos < 156 and mouseypos < 156:
        print("1")
        screen.blit(rendered, (20,15))
        pygame.display.update(10,10,166,166)


    # display what’s drawn. this might change.
    pygame.display.update()

    # run at 20 fps
    clock.tick(20)

# close the window and quit
pygame.quit()
