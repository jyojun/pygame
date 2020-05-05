import pgzrun
import pygame

pygame.init()

font = pygame.font.Font(None, 36)


win = pygame.display.set_mode((800,700))
win.fill((255,255,255))
pygame.display.set_caption('Connect4')

board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

firstone = pygame.draw.rect(win, (0,0,255), (50,50,100,100))
firsttwo = pygame.draw.rect(win, (0,0,255), (150,50,100,100))
firstthree = pygame.draw.rect(win, (0,0,255), (250,50,100,100))
firstfour = pygame.draw.rect(win, (0,0,255), (350,50,100,100))
firstfive = pygame.draw.rect(win, (0,0,255), (450,50,100,100))
firstsix = pygame.draw.rect(win, (0,0,255), (550,50,100,100))
firstseven = pygame.draw.rect(win, (0,0,255), (650,50,100,100))

secondone = pygame.draw.rect(win, (0,0,255), (50,150,100,100))
secondtwo = pygame.draw.rect(win, (0,0,255), (150,150,100,100))
secondthree = pygame.draw.rect(win, (0,0,255), (250,150,100,100))
secondfour = pygame.draw.rect(win, (0,0,255), (350,150,100,100))
secondfive = pygame.draw.rect(win, (0,0,255), (450,150,100,100))
secondsix = pygame.draw.rect(win, (0,0,255), (550,150,100,100))
secondseven = pygame.draw.rect(win, (0,0,255), (650,150,100,100))

thirdone = pygame.draw.rect(win, (0,0,255), (50,250,100,100))
thirdtwo = pygame.draw.rect(win, (0,0,255), (150,250,100,100))
thirdthree = pygame.draw.rect(win, (0,0,255), (250,250,100,100))
thirdfour = pygame.draw.rect(win, (0,0,255), (350,250,100,100))
thirdfive = pygame.draw.rect(win, (0,0,255), (450,250,100,100))
thirdsix = pygame.draw.rect(win, (0,0,255), (550,250,100,100))
thirdseven = pygame.draw.rect(win, (0,0,255), (650,250,100,100))

fourthone = pygame.draw.rect(win, (0,0,255), (50,350,100,100))
fourthtwo = pygame.draw.rect(win, (0,0,255), (150,350,100,100))
fourththree = pygame.draw.rect(win, (0,0,255), (250,350,100,100))
fourthfour = pygame.draw.rect(win, (0,0,255), (350,350,100,100))
fourthfive = pygame.draw.rect(win, (0,0,255), (450,350,100,100))
fourthsix = pygame.draw.rect(win, (0,0,255), (550,350,100,100))
fourthseven = pygame.draw.rect(win, (0,0,255), (650,350,100,100))

fifthone = pygame.draw.rect(win, (0,0,255), (50,450,100,100))
fifthtwo = pygame.draw.rect(win, (0,0,255), (150,450,100,100))
fifththree = pygame.draw.rect(win, (0,0,255), (250,450,100,100))
fifthfour = pygame.draw.rect(win, (0,0,255), (350,450,100,100))
fifthfive = pygame.draw.rect(win, (0,0,255), (450,450,100,100))
fifthsix = pygame.draw.rect(win, (0,0,255), (550,450,100,100))
fifthseven = pygame.draw.rect(win, (0,0,255), (650,450,100,100))

sixthone = pygame.draw.rect(win, (0,0,255), (50,550,100,100))
sixthtwo = pygame.draw.rect(win, (0,0,255), (150,550,100,100))
sixththree = pygame.draw.rect(win, (0,0,255), (250,550,100,100))
sixthfour = pygame.draw.rect(win, (0,0,255), (350,550,100,100))
sixthfive = pygame.draw.rect(win, (0,0,255), (450,550,100,100))
sixthsix = pygame.draw.rect(win, (0,0,255), (550,550,100,100))
sixthseven = pygame.draw.rect(win, (0,0,255), (650,550,100,100))

#circle
firstonecircle = pygame.draw.circle(win, (255,255,255), (100,100),40)
firsttwocircle = pygame.draw.circle(win, (255,255,255), (200,100),40)
firstthreecircle = pygame.draw.circle(win, (255,255,255), (300,100),40)
firstfourcircle = pygame.draw.circle(win, (255,255,255), (400,100),40)
firstfivecircle = pygame.draw.circle(win, (255,255,255), (500,100),40)
firstsixcircle = pygame.draw.circle(win, (255,255,255), (600,100),40)
firstsevencircle = pygame.draw.circle(win, (255,255,255), (700,100),40)

secondonecircle = pygame.draw.circle(win, (255,255,255), (100,200),40)
secondtwocircle = pygame.draw.circle(win, (255,255,255), (200,200),40)
secondthreecircle = pygame.draw.circle(win, (255,255,255), (300,200),40)
secondfourcircle = pygame.draw.circle(win, (255,255,255), (400,200),40)
secondfivecircle = pygame.draw.circle(win, (255,255,255), (500,200),40)
secondsixcircle = pygame.draw.circle(win, (255,255,255), (600,200),40)
secondsevencircle = pygame.draw.circle(win, (255,255,255), (700,200),40)

thirdonecircle = pygame.draw.circle(win, (255,255,255), (100,300),40)
thirdtwocircle = pygame.draw.circle(win, (255,255,255), (200,300),40)
thirdthreecircle = pygame.draw.circle(win, (255,255,255), (300,300),40)
thirdfourcircle = pygame.draw.circle(win, (255,255,255), (400,300),40)
thirdfivecircle = pygame.draw.circle(win, (255,255,255), (500,300),40)
thirdsixcircle = pygame.draw.circle(win, (255,255,255), (600,300),40)
thirdsevencircle = pygame.draw.circle(win, (255,255,255), (700,300),40)

fourthone = pygame.draw.circle(win, (255,255,255), (100,400),40)
fourthtwo = pygame.draw.circle(win, (255,255,255), (200,400),40)
fourththree = pygame.draw.circle(win, (255,255,255), (300,400),40)
fourthfour = pygame.draw.circle(win, (255,255,255), (400,400),40)
fourthfive = pygame.draw.circle(win, (255,255,255), (500,400),40)
fourthsix = pygame.draw.circle(win, (255,255,255), (600,400),40)
fourthseven = pygame.draw.circle(win, (255,255,255), (700,400),40)

fifthonecircle = pygame.draw.circle(win, (255,255,255), (100,500),40)
fifthtwocircle = pygame.draw.circle(win, (255,255,255), (200,500),40)
fifththreecircle = pygame.draw.circle(win, (255,255,255), (300,500),40)
fifthfourcircle = pygame.draw.circle(win, (255,255,255), (400,500),40)
fifthfivecircle = pygame.draw.circle(win, (255,255,255), (500,500),40)
fifthsixcircle = pygame.draw.circle(win, (255,255,255), (600,500),40)
fifthsevencircle = pygame.draw.circle(win, (255,255,255), (700,500),40)

sixthonecircle = pygame.draw.circle(win, (255,255,255), (100,600),40)
sixthtwocircle = pygame.draw.circle(win, (255,255,255), (200,600),40)
sixththreecircle = pygame.draw.circle(win, (255,255,255), (300,600),40)
sixthfourcircle = pygame.draw.circle(win, (255,255,255), (400,600),40)
sixthfivecircle = pygame.draw.circle(win, (255,255,255), (500,600),40)
sixthsixcircle = pygame.draw.circle(win, (255,255,255), (600,600),40)
sixthsevencircle = pygame.draw.circle(win, (255,255,255), (700,600),40)

draw_color = 'yellow'

first_count = 0
second_count = 0
third_count = 0
fourth_count = 0
fifth_count = 0
sixth_count = 0
seventh_count = 0

#board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

        
def win_check(num):
    
    # check horizontal locations for win 
    for c in range(4):
        for r in range(6):
            if board[r][c] == num and board[r][c+1] == num and board[r][c+2] == num and board[r][c+3] == num:
                print("horizontal win")
                return True
            
    # check vertical locations for win
    for c in range(7):
        for r in range(3):
            if board[r][c] == num and board[r+1][c] == num and board[r+2][c] == num and board[r+3][c] == num:
                print("vertical win")
                return True

    # Check positively sloped diaganols
    for c in range(4):
        for r in range(3):
            if board[r][c] == num and board[r+1][c+1] == num and board[r+2][c+2] == num and board[r+3][c+3] == num:
                print("positively sloped diaganols win")
                return True

    # Check negatively sloped diaganols
    for c in range(4):
        for r in range(3):
            if board[r][3-c] == num and board[r+1][3-(c+1)] == num and board[r+2][3-(c+2)] == num and board[r+3][3-(c+3)] == num:
                print("negatively sloped diaganols win")
                return True
    
    


#Main Loop
run = True
won = False
while run:
    
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                won = False

                first_count = 0
                second_count = 0
                third_count = 0
                fourth_count = 0
                fifth_count = 0
                sixth_count = 0
                seventh_count = 0

                board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

                #circle
                firstonecircle = pygame.draw.circle(win, (255,255,255), (100,100),40)
                firsttwocircle = pygame.draw.circle(win, (255,255,255), (200,100),40)
                firstthreecircle = pygame.draw.circle(win, (255,255,255), (300,100),40)
                firstfourcircle = pygame.draw.circle(win, (255,255,255), (400,100),40)
                firstfivecircle = pygame.draw.circle(win, (255,255,255), (500,100),40)
                firstsixcircle = pygame.draw.circle(win, (255,255,255), (600,100),40)
                firstsevencircle = pygame.draw.circle(win, (255,255,255), (700,100),40)

                secondonecircle = pygame.draw.circle(win, (255,255,255), (100,200),40)
                secondtwocircle = pygame.draw.circle(win, (255,255,255), (200,200),40)
                secondthreecircle = pygame.draw.circle(win, (255,255,255), (300,200),40)
                secondfourcircle = pygame.draw.circle(win, (255,255,255), (400,200),40)
                secondfivecircle = pygame.draw.circle(win, (255,255,255), (500,200),40)
                secondsixcircle = pygame.draw.circle(win, (255,255,255), (600,200),40)
                secondsevencircle = pygame.draw.circle(win, (255,255,255), (700,200),40)

                thirdonecircle = pygame.draw.circle(win, (255,255,255), (100,300),40)
                thirdtwocircle = pygame.draw.circle(win, (255,255,255), (200,300),40)
                thirdthreecircle = pygame.draw.circle(win, (255,255,255), (300,300),40)
                thirdfourcircle = pygame.draw.circle(win, (255,255,255), (400,300),40)
                thirdfivecircle = pygame.draw.circle(win, (255,255,255), (500,300),40)
                thirdsixcircle = pygame.draw.circle(win, (255,255,255), (600,300),40)
                thirdsevencircle = pygame.draw.circle(win, (255,255,255), (700,300),40)

                fourthone = pygame.draw.circle(win, (255,255,255), (100,400),40)
                fourthtwo = pygame.draw.circle(win, (255,255,255), (200,400),40)
                fourththree = pygame.draw.circle(win, (255,255,255), (300,400),40)
                fourthfour = pygame.draw.circle(win, (255,255,255), (400,400),40)
                fourthfive = pygame.draw.circle(win, (255,255,255), (500,400),40)
                fourthsix = pygame.draw.circle(win, (255,255,255), (600,400),40)
                fourthseven = pygame.draw.circle(win, (255,255,255), (700,400),40)

                fifthonecircle = pygame.draw.circle(win, (255,255,255), (100,500),40)
                fifthtwocircle = pygame.draw.circle(win, (255,255,255), (200,500),40)
                fifththreecircle = pygame.draw.circle(win, (255,255,255), (300,500),40)
                fifthfourcircle = pygame.draw.circle(win, (255,255,255), (400,500),40)
                fifthfivecircle = pygame.draw.circle(win, (255,255,255), (500,500),40)
                fifthsixcircle = pygame.draw.circle(win, (255,255,255), (600,500),40)
                fifthsevencircle = pygame.draw.circle(win, (255,255,255), (700,500),40)

                sixthonecircle = pygame.draw.circle(win, (255,255,255), (100,600),40)
                sixthtwocircle = pygame.draw.circle(win, (255,255,255), (200,600),40)
                sixththreecircle = pygame.draw.circle(win, (255,255,255), (300,600),40)
                sixthfourcircle = pygame.draw.circle(win, (255,255,255), (400,600),40)
                sixthfivecircle = pygame.draw.circle(win, (255,255,255), (500,600),40)
                sixthsixcircle = pygame.draw.circle(win, (255,255,255), (600,600),40)
                sixthsevencircle = pygame.draw.circle(win, (255,255,255), (700,600),40)

                
            
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if won != True:
                

                if (firstone.collidepoint(pos) or secondone.collidepoint(pos) or thirdone.collidepoint(pos) or fourthone.collidepoint(pos) or fifthone.collidepoint(pos) or sixthone.collidepoint(pos)) and first_count != 6:
                    if draw_color == 'red':
                        if first_count == 0:
                            pygame.draw.circle(win, (255,0,0), (100,600),40)
                            board[5][0]=1
                            first_count = 1
                        elif first_count == 1:
                            pygame.draw.circle(win, (255,0,0), (100,500),40)
                            board[4][0]=1
                            first_count = 2
                        elif first_count == 2:
                            pygame.draw.circle(win, (255,0,0), (100,400),40)
                            board[3][0]=1
                            first_count = 3
                        elif first_count == 3:
                            pygame.draw.circle(win, (255,0,0), (100,300),40)
                            board[2][0]=1
                            first_count = 4
                        elif first_count == 4:
                            pygame.draw.circle(win, (255,0,0), (100,200),40)
                            board[1][0]=1
                            first_count = 5
                        elif first_count == 5:
                            pygame.draw.circle(win, (255,0,0), (100,100),40)
                            board[0][0]=1
                            first_count = 6

                        draw_color = 'yellow'

                    elif draw_color == 'yellow':
                        if first_count == 0:
                            pygame.draw.circle(win, (255,255,0), (100,600),40)
                            board[5][0]=2
                            first_count = 1
                        elif first_count == 1:
                            pygame.draw.circle(win, (255,255,0), (100,500),40)
                            board[4][0]=2
                            first_count = 2
                        elif first_count == 2:
                            pygame.draw.circle(win, (255,255,0), (100,400),40)
                            board[3][0]=2
                            first_count = 3
                        elif first_count == 3:
                            pygame.draw.circle(win, (255,255,0), (100,300),40)
                            board[2][0]=2
                            first_count = 4
                        elif first_count == 4:
                            pygame.draw.circle(win, (255,255,0), (100,200),40)
                            board[1][0]=2
                            first_count = 5
                        elif first_count == 5:
                            pygame.draw.circle(win, (255,255,0), (100,100),40)
                            board[0][0]=2
                            first_count = 6

                        draw_color = 'red'

                if (firsttwo.collidepoint(pos) or secondtwo.collidepoint(pos) or thirdtwo.collidepoint(pos) or fourthtwo.collidepoint(pos) or fifthtwo.collidepoint(pos) or sixthtwo.collidepoint(pos)) and second_count != 6:
                    if draw_color == 'red':
                        if second_count == 0:
                            pygame.draw.circle(win, (255,0,0), (200,600),40)
                            board[5][1]=1
                            second_count = 1
                        elif second_count == 1:
                            pygame.draw.circle(win, (255,0,0), (200,500),40)
                            board[4][1]=1
                            second_count = 2
                        elif second_count == 2:
                            pygame.draw.circle(win, (255,0,0), (200,400),40)
                            board[3][1]=1
                            second_count = 3
                        elif second_count == 3:
                            pygame.draw.circle(win, (255,0,0), (200,300),40)
                            board[2][1]=1
                            second_count = 4
                        elif second_count == 4:
                            pygame.draw.circle(win, (255,0,0), (200,200),40)
                            board[1][1]=1
                            second_count = 5
                        elif second_count == 5:
                            pygame.draw.circle(win, (255,0,0), (200,100),40)
                            board[0][1]=1
                            second_count = 6

                        draw_color = 'yellow'

                    elif draw_color == 'yellow':
                        if second_count == 0:
                            pygame.draw.circle(win, (255,255,0), (200,600),40)
                            board[5][1]=2
                            second_count = 1
                        elif second_count == 1:
                            pygame.draw.circle(win, (255,255,0), (200,500),40)
                            board[4][1]=2
                            second_count = 2
                        elif second_count == 2:
                            pygame.draw.circle(win, (255,255,0), (200,400),40)
                            board[3][1]=2
                            second_count = 3
                        elif second_count == 3:
                            pygame.draw.circle(win, (255,255,0), (200,300),40)
                            board[2][1]=2
                            second_count = 4
                        elif second_count == 4:
                            pygame.draw.circle(win, (255,255,0), (200,200),40)
                            board[1][1]=2
                            second_count = 5
                        elif second_count == 5:
                            pygame.draw.circle(win, (255,255,0), (200,100),40)
                            board[0][1]=2
                            second_count = 6

                        draw_color = 'red'

                if (firstthree.collidepoint(pos) or secondthree.collidepoint(pos) or thirdthree.collidepoint(pos) or fourththree.collidepoint(pos) or fifththree.collidepoint(pos) or sixththree.collidepoint(pos)) and third_count != 6:
                    if draw_color == 'red':
                        if third_count == 0:
                            pygame.draw.circle(win, (255,0,0), (300,600),40)
                            board[5][2]=1
                            third_count = 1
                        elif third_count == 1:
                            pygame.draw.circle(win, (255,0,0), (300,500),40)
                            board[4][2]=1
                            third_count = 2
                        elif third_count == 2:
                            pygame.draw.circle(win, (255,0,0), (300,400),40)
                            board[3][2]=1
                            third_count = 3
                        elif third_count == 3:
                            pygame.draw.circle(win, (255,0,0), (300,300),40)
                            board[2][2]=1
                            third_count = 4
                        elif third_count == 4:
                            pygame.draw.circle(win, (255,0,0), (300,200),40)
                            board[1][2]=1
                            third_count = 5
                        elif third_count == 5:
                            pygame.draw.circle(win, (255,0,0), (300,100),40)
                            board[0][2]=1
                            third_count = 6

                        draw_color = 'yellow'

                    elif draw_color == 'yellow':
                        if third_count == 0:
                            pygame.draw.circle(win, (255,255,0), (300,600),40)
                            board[5][2]=2
                            third_count = 1
                        elif third_count == 1:
                            pygame.draw.circle(win, (255,255,0), (300,500),40)
                            board[4][2]=2
                            third_count = 2
                        elif third_count == 2:
                            pygame.draw.circle(win, (255,255,0), (300,400),40)
                            board[3][2]=2
                            third_count = 3
                        elif third_count == 3:
                            pygame.draw.circle(win, (255,255,0), (300,300),40)
                            board[2][2]=2
                            third_count = 4
                        elif third_count == 4:
                            pygame.draw.circle(win, (255,255,0), (300,200),40)
                            board[1][2]=2
                            third_count = 5
                        elif third_count == 5:
                            pygame.draw.circle(win, (255,255,0), (300,100),40)
                            board[0][2]=2
                            third_count = 6

                        draw_color = 'red'

                if (firstfour.collidepoint(pos) or secondfour.collidepoint(pos) or thirdfour.collidepoint(pos) or fourthfour.collidepoint(pos) or fifthfour.collidepoint(pos) or sixthfour.collidepoint(pos)) and fourth_count != 6:
                    if draw_color == 'red':
                        if fourth_count == 0:
                            pygame.draw.circle(win, (255,0,0), (400,600),40)
                            board[5][3]=1
                            fourth_count = 1
                        elif fourth_count == 1:
                            pygame.draw.circle(win, (255,0,0), (400,500),40)
                            board[4][3]=1
                            fourth_count = 2
                        elif fourth_count == 2:
                            pygame.draw.circle(win, (255,0,0), (400,400),40)
                            board[3][3]=1
                            fourth_count = 3
                        elif fourth_count == 3:
                            pygame.draw.circle(win, (255,0,0), (400,300),40)
                            board[2][3]=1
                            fourth_count = 4
                        elif fourth_count == 4:
                            pygame.draw.circle(win, (255,0,0), (400,200),40)
                            board[1][3]=1
                            fourth_count = 5
                        elif fourth_count == 5:
                            pygame.draw.circle(win, (255,0,0), (400,100),40)
                            board[0][3]=1
                            fourth_count = 6

                        draw_color = 'yellow'

                    elif draw_color == 'yellow':
                        if fourth_count == 0:
                            pygame.draw.circle(win, (255,255,0), (400,600),40)
                            board[5][3]=2
                            fourth_count = 1
                        elif fourth_count == 1:
                            pygame.draw.circle(win, (255,255,0), (400,500),40)
                            board[4][3]=2
                            fourth_count = 2
                        elif fourth_count == 2:
                            pygame.draw.circle(win, (255,255,0), (400,400),40)
                            board[3][3]=2
                            fourth_count = 3
                        elif fourth_count == 3:
                            pygame.draw.circle(win, (255,255,0), (400,300),40)
                            board[2][3]=2
                            fourth_count = 4
                        elif fourth_count == 4:
                            pygame.draw.circle(win, (255,255,0), (400,200),40)
                            board[1][3]=2
                            fourth_count = 5
                        elif fourth_count == 5:
                            pygame.draw.circle(win, (255,255,0), (400,100),40)
                            board[0][3]=2
                            fourth_count = 6

                        draw_color = 'red'

                if (firstfive.collidepoint(pos) or secondfive.collidepoint(pos) or thirdfive.collidepoint(pos) or fourthfive.collidepoint(pos) or fifthfive.collidepoint(pos) or sixthfive.collidepoint(pos)) and fifth_count != 6:
                    if draw_color == 'red':
                        if fifth_count == 0:
                            pygame.draw.circle(win, (255,0,0), (500,600),40)
                            board[5][4]=1
                            fifth_count = 1
                        elif fifth_count == 1:
                            pygame.draw.circle(win, (255,0,0), (500,500),40)
                            board[4][4]=1
                            fifth_count = 2
                        elif fifth_count == 2:
                            pygame.draw.circle(win, (255,0,0), (500,400),40)
                            board[3][4]=1
                            fifth_count = 3
                        elif fifth_count == 3:
                            pygame.draw.circle(win, (255,0,0), (500,300),40)
                            board[2][4]=1
                            fifth_count = 4
                        elif fifth_count == 4:
                            pygame.draw.circle(win, (255,0,0), (500,200),40)
                            board[1][4]=1
                            fifth_count = 5
                        elif fifth_count == 5:
                            pygame.draw.circle(win, (255,0,0), (500,100),40)
                            board[0][4]=1
                            fifth_count = 6

                        draw_color = 'yellow'

                    elif draw_color == 'yellow':
                        if fifth_count == 0:
                            pygame.draw.circle(win, (255,255,0), (500,600),40)
                            board[5][4]=2
                            fifth_count = 1
                        elif fifth_count == 1:
                            pygame.draw.circle(win, (255,255,0), (500,500),40)
                            board[4][4]=2
                            fifth_count = 2
                        elif fifth_count == 2:
                            pygame.draw.circle(win, (255,255,0), (500,400),40)
                            board[3][4]=2
                            fifth_count = 3
                        elif fifth_count == 3:
                            pygame.draw.circle(win, (255,255,0), (500,300),40)
                            board[2][4]=2
                            fifth_count = 4
                        elif fifth_count == 4:
                            pygame.draw.circle(win, (255,255,0), (500,200),40)
                            board[1][4]=2
                            fifth_count = 5
                        elif fifth_count == 5:
                            pygame.draw.circle(win, (255,255,0), (500,100),40)
                            board[0][4]=2
                            fifth_count = 6

                        draw_color = 'red'

                if (firstsix.collidepoint(pos) or secondsix.collidepoint(pos) or thirdsix.collidepoint(pos) or fourthsix.collidepoint(pos) or fifthsix.collidepoint(pos) or sixthsix.collidepoint(pos)) and sixth_count != 6:
                    if draw_color == 'red':
                        if sixth_count == 0:
                            pygame.draw.circle(win, (255,0,0), (600,600),40)
                            board[5][5]=1
                            sixth_count = 1
                        elif sixth_count == 1:
                            pygame.draw.circle(win, (255,0,0), (600,500),40)
                            board[4][5]=1
                            sixth_count = 2
                        elif sixth_count == 2:
                            pygame.draw.circle(win, (255,0,0), (600,400),40)
                            board[3][5]=1
                            sixth_count = 3
                        elif sixth_count == 3:
                            pygame.draw.circle(win, (255,0,0), (600,300),40)
                            board[2][5]=1
                            sixth_count = 4
                        elif sixth_count == 4:
                            pygame.draw.circle(win, (255,0,0), (600,200),40)
                            board[1][5]=1
                            sixth_count = 5
                        elif sixth_count == 5:
                            pygame.draw.circle(win, (255,0,0), (600,100),40)
                            board[0][5]=1
                            sixth_count = 6

                        draw_color = 'yellow'

                    elif draw_color == 'yellow':
                        if sixth_count == 0:
                            pygame.draw.circle(win, (255,255,0), (600,600),40)
                            board[5][5]=2
                            sixth_count = 1
                        elif sixth_count == 1:
                            pygame.draw.circle(win, (255,255,0), (600,500),40)
                            board[4][5]=2
                            sixth_count = 2
                        elif sixth_count == 2:
                            pygame.draw.circle(win, (255,255,0), (600,400),40)
                            board[3][5]=2
                            sixth_count = 3
                        elif sixth_count == 3:
                            pygame.draw.circle(win, (255,255,0), (600,300),40)
                            board[2][5]=2
                            sixth_count = 4
                        elif sixth_count == 4:
                            pygame.draw.circle(win, (255,255,0), (600,200),40)
                            board[1][5]=2
                            sixth_count = 5
                        elif sixth_count == 5:
                            pygame.draw.circle(win, (255,255,0), (600,100),40)
                            board[0][5]=2
                            sixth_count = 6

                        draw_color = 'red'

                if (firstseven.collidepoint(pos) or secondseven.collidepoint(pos) or thirdseven.collidepoint(pos) or fourthseven.collidepoint(pos) or fifthseven.collidepoint(pos) or sixthseven.collidepoint(pos)) and seventh_count != 6:
                    if draw_color == 'red':
                        if seventh_count == 0:
                            pygame.draw.circle(win, (255,0,0), (700,600),30)
                            board[5][6]=1
                            seventh_count = 1
                        elif seventh_count == 1:
                            pygame.draw.circle(win, (255,0,0), (700,500),30)
                            board[4][6]=1
                            seventh_count = 2
                        elif seventh_count == 2:
                            pygame.draw.circle(win, (255,0,0), (700,400),30)
                            board[3][6]=1
                            seventh_count = 3
                        elif seventh_count == 3:
                            pygame.draw.circle(win, (255,0,0), (700,300),30)
                            board[2][6]=1
                            seventh_count = 4
                        elif seventh_count == 4:
                            pygame.draw.circle(win, (255,0,0), (700,200),30)
                            board[1][6]=1
                            seventh_count = 5
                        elif seventh_count == 5:
                            pygame.draw.circle(win, (255,0,0), (700,100),30)
                            board[0][6]=1
                            seventh_count = 6

                        draw_color = 'yellow'

                    elif draw_color == 'yellow':
                        if seventh_count == 0:
                            pygame.draw.circle(win, (255,255,0), (700,600),30)
                            board[5][6]=2
                            seventh_count = 1
                        elif seventh_count == 1:
                            pygame.draw.circle(win, (255,255,0), (700,500),30)
                            board[4][6]=2
                            seventh_count = 2
                        elif seventh_count == 2:
                            pygame.draw.circle(win, (255,255,0), (700,400),30)
                            board[3][6]=2
                            seventh_count = 3
                        elif seventh_count == 3:
                            pygame.draw.circle(win, (255,255,0), (700,300),30)
                            board[2][6]=2
                            seventh_count = 4
                        elif seventh_count == 4:
                            pygame.draw.circle(win, (255,255,0), (700,200),30)
                            board[1][6]=2
                            seventh_count = 5
                        elif seventh_count == 5:
                            pygame.draw.circle(win, (255,255,0), (700,100),30)
                            board[0][6]=2
                            seventh_count = 6

                        draw_color = 'red'

    if win_check(1):
        won = True
        
    if win_check(2):
        won = True


    #updates screen with new shapes        
    pygame.display.update() 


pygame.quit()
pgzrun.go()
