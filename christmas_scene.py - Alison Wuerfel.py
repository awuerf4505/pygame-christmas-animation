# Computer Programming 1
# Unit 11 - Graphics
#
# Christmas Setting


# Imports
import pygame
import random
import math

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Christmas Setting"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
GREY = (114, 114, 114)
LIGHTGREY = (200, 200, 200)
RED = (200, 0, 0)
BLACK = (0,0,0)
SNOW = (241, 245, 251)
DARKRED = (136, 0, 0)
DARKGREEN = (0, 136, 0)
DARKBLUE = (0, 0, 136)
def draw_snow(x, y):
    pygame.draw.ellipse(screen, SNOW, [x, y + 6, 10 , 10])
'''make snow'''
snow = []
for i in range(800):
    x = random.randrange(10, 1600)
    y = random.randrange(0,800)
    snow.append([x, y])


def draw_cloud(x, y):
    pygame.draw.ellipse(screen, GREY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GREY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GREY, [x + 20, y + 20, 60, 40])






''' make clouds '''
clouds = []
for i in range(800):
    x = random.randrange(-100, 1600)
    y = random.randrange(0,20)
    clouds.append([x, y])



lights = True
daytime = True



green_lights = []
for n in range(35):
    x = random.randrange(25, 370)
    y = random.randrange(345, 370)
    r = random.randrange(10, 11)
    green_lights.append([x, y, r, r])
blue_lights = []
for n in range(35):
    x = random.randrange(25, 370)
    y = random.randrange(345, 370)
    r = random.randrange(10, 11)
    blue_lights.append([x, y, r, r])
red_lights = []
for n in range(35):
    x = random.randrange(25, 370)
    y = random.randrange(345, 370)
    r = random.randrange(10, 11)
    red_lights.append([x, y, r, r])
    
# Game loop
done = False
ticks = 0
boxx= 600
boxy = 400
linex= 605
liney = 410
linext = 605
lineyt = 400
horzx = 600
horzy = 405
horzxt = 610
horzyt = 405

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            if event.key == pygame.K_LEFT:
                boxx = boxx - 6
                linex = linex - 6
                linext = linext - 6
                horzx = horzx - 6
                horzxt = horzxt - 6
            if event.key == pygame.K_RIGHT:
                boxx = boxx + 6
                linex = linex + 6
                linext = linext + 6
                horzx = horzx + 6
                horzxt = horzxt + 6
            if event.key == pygame.K_UP:
                boxy = boxy - 6
                liney = liney - 6
                lineyt = lineyt - 6
                horzy = horzy - 6
                horzyt = horzyt - 6
            if event.key == pygame.K_DOWN:
                boxy = boxy + 6
                liney = liney + 6
                lineyt = lineyt + 6
                horzy = horzy + 6
                horzyt = horzyt + 6

    state = pygame.key.get_pressed()

    left = state[pygame.K_LEFT]
    right = state[pygame.K_RIGHT]
    up = state[pygame.K_UP]
    down = state[pygame.K_DOWN]

    # Game logic

    
    frame = ticks // 10
    
    ticks += 1

    if ticks >= 30:
        ticks = 0
        
    ''' move snow '''
    for c in snow:
        c[1] += random.randint(2, 4) 
        c[0] -= random.randint(2, 3)

        if c[1] > 800:
            c[0] = random.randrange(000, 1500)
            c[1] = random.randrange(-200, 0)
    ''' move clouds '''
    for c in clouds:
        c[0] -= 1

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 35)


  
    '''set sky color'''
    if daytime:
        sky = LIGHTGREY
    else:
        sky = BLACK


   
    # Drawing code


    ''' sky '''
    screen.fill(sky)

    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])
    if daytime== False:
            pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])
            pygame.draw.ellipse(screen, BLACK, [610, 75, 100, 100])


        

  
    ''' grass '''
    pygame.draw.rect(screen, SNOW, [0, 400, 800, 200])
    
    for c in snow:
        draw_snow(c[0], c[1])
        
    ''' fence '''
    y = 380
    for x in range(5, 800, 35):
        pygame.draw.polygon(screen, BLACK, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, BLACK, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, BLACK, [0, 410], [800, 410], 5)

     


    ''' barn'''
    pygame.draw.rect(screen, WHITE, [20, 350, 350, 200])
    pygame.draw.rect(screen, BLACK, [20, 350, 350, 200], 1)
    '''cord'''
    y = 335
    for x in range (-30, 315, 30):
        pygame.draw.ellipse(screen, GREY, [x+40, 335, 40, 40], 3)
    '''lights'''    
    for l in green_lights:
        pygame.draw.ellipse(screen, GREEN, l)
        if frame == 0:
           pygame.draw.ellipse(screen, DARKGREEN, l)

    for l in blue_lights:
        pygame.draw.ellipse(screen, BLUE, l)
        if frame == 1:
           pygame.draw.ellipse(screen, DARKBLUE, l)

            
    for l in red_lights:
        pygame.draw.ellipse(screen, RED, l)
        if frame == 2:
           pygame.draw.ellipse(screen, DARKRED, l)

            

    '''roof and door'''
    pygame.draw.polygon(screen, BLACK, [[10,350], [192, 200], [375,350]])
    if daytime == False:
        pygame.draw.polygon(screen, BLACK, [[10,350], [192, 200], [375,350]])
        pygame.draw.polygon(screen, WHITE, [[10,350], [192, 200], [375,350]], 5)
    pygame.draw.rect(screen, RED, [142, 400, 100, 150])
    pygame.draw.rect(screen, DARKRED, [147, 405, 40, 65], 5)
    pygame.draw.rect(screen, DARKRED, [198, 405, 40, 65], 5)
    pygame.draw.rect(screen, DARKRED, [198, 480, 40, 65], 5)
    pygame.draw.rect(screen, DARKRED, [147, 480, 40, 65], 5)
    pygame.draw.ellipse(screen, YELLOW, [230, 470, 10, 10])



    ''' windows and wreaths'''
    pygame.draw.rect(screen, BLACK, [262, 408, 75, 100])
    if daytime == True:
        pygame.draw.rect(screen, YELLOW, [262, 408, 75, 100])
        pygame.draw.rect(screen, BLACK, [262, 408, 75, 100], 1)

    pygame.draw.rect(screen, BLACK, [49, 408, 75, 100])
    if daytime == True:
                pygame.draw.rect(screen, YELLOW, [49, 408, 75, 100])
                pygame.draw.rect(screen, BLACK, [49, 408, 75, 100], 1)
            
    pygame.draw.line(screen, WHITE, [300, 409], [300, 505], 5)
    pygame.draw.line(screen, WHITE, [263, 458], [335, 458], 5)
    pygame.draw.line(screen, WHITE, [87, 409], [87, 505], 5)
    pygame.draw.line(screen, WHITE, [50, 458], [122, 458], 5)
    pygame.draw.ellipse(screen, GREEN, [280, 438, 40, 40], 8)
    pygame.draw.ellipse(screen, GREEN, [67, 438, 40, 40], 8)



    '''ribbon one'''
    pygame.draw.rect(screen, RED, [83 , 470, 9, 10])
    pygame.draw.polygon(screen, RED, [[73, 460],[73, 480],[85, 475]])
    pygame.draw.polygon(screen, RED, [[101, 460],[101, 480],[87, 475]])
    pygame.draw.line(screen, RED, [85, 480], [80, 487], 5)
    pygame.draw.line(screen, RED, [90, 480], [95, 487], 5)


    '''ribbon two'''
    pygame.draw.rect(screen, RED, [296 , 470, 9, 10])
    pygame.draw.polygon(screen, RED, [[286, 460],[286, 480],[298, 475]])
    pygame.draw.polygon(screen, RED, [[314, 460],[314, 480],[298, 475]])
    pygame.draw.line(screen, RED, [298, 480], [293, 487], 5)
    pygame.draw.line(screen, RED, [303, 480], [308, 487], 5)


    '''lights deer'''
    pygame.draw.rect(screen, BLACK, [470, 470, 50, 20], 3)
    if daytime == False:
            pygame.draw.rect(screen, YELLOW, [470, 470, 50, 20], 3)
    pygame.draw.line(screen, BLACK, [470, 490], [470, 528], 3)
    if daytime == False:
            pygame.draw.line(screen, YELLOW, [470, 490], [470, 528], 3)
    pygame.draw.line(screen, BLACK, [477, 490], [477, 515], 3)
    if daytime == False:
            pygame.draw.line(screen, YELLOW, [477, 490], [477, 515], 3)
    pygame.draw.line(screen, BLACK, [510, 490], [510, 515], 3)
    if daytime == False:
            pygame.draw.line(screen, YELLOW, [510, 490], [510, 515], 3)
    pygame.draw.line(screen, BLACK, [517, 490], [517, 528], 3)
    if daytime == False:
            pygame.draw.line(screen, YELLOW, [517, 490], [517, 528], 3)
    pygame.draw.line(screen, BLACK, [520, 470], [535, 450], 3)
    if daytime == False:
            pygame.draw.line(screen, YELLOW, [520, 470], [535, 450], 3)
    if frame == 0:
        pygame.draw.line(screen, SNOW, [520, 470], [535, 450], 3)
        pygame.draw.line(screen, BLACK, [520, 470], [535, 490], 3)
    if daytime == False:
        if frame == 0:
            pygame.draw.line(screen, SNOW, [520, 470], [535, 450], 3)
            pygame.draw.line(screen, YELLOW, [520, 470], [535, 490], 3)       
    pygame.draw.ellipse(screen, BLACK, [530, 445, 40, 20], 3)
    if daytime == False:
            pygame.draw.ellipse(screen, YELLOW, [530, 445, 40, 20], 3)        
    if frame == 0:
        pygame.draw.ellipse(screen, SNOW, [530, 445, 40, 20], 3)
        pygame.draw.ellipse(screen, BLACK, [530, 485, 20, 40], 3)
    if daytime == False:
        if frame == 0:
            pygame.draw.ellipse(screen, SNOW, [530, 445, 40, 20], 3)
            pygame.draw.ellipse(screen, YELLOW, [530, 485, 20, 40], 3)  
    pygame.draw.line(screen, BLACK, [540, 455], [530, 425], 3)
    if daytime == False:
            pygame.draw.line(screen, YELLOW, [540, 455], [530, 425], 3)
    if frame == 0:
        pygame.draw.line(screen, SNOW, [540, 455], [530, 425], 3)
        pygame.draw.line(screen, BLACK, [540, 495], [565, 478], 3)
    if daytime == False:
        if frame == 0:
            pygame.draw.line(screen, SNOW, [540, 455], [530, 425], 3)
            pygame.draw.line(screen, YELLOW, [540, 495], [565, 478], 3)
    pygame.draw.line(screen, BLACK, [533, 435], [523, 430], 3)
    if daytime == False:
            pygame.draw.line(screen, YELLOW, [533, 435], [523, 430], 3)
    if frame == 0:
        pygame.draw.line(screen, SNOW, [533, 435], [523, 430], 3)
        pygame.draw.line(screen, BLACK, [560, 470], [555, 485], 3)
    if daytime == False:
        if frame == 0:
            pygame.draw.line(screen, SNOW, [533, 435], [523, 430], 3)
            pygame.draw.line(screen, YELLOW, [560, 470], [555, 485], 3)        
    pygame.draw.line(screen, BLACK, [537, 440], [547, 430], 3)
    if daytime == False:
            pygame.draw.line(screen, YELLOW, [537, 440], [547, 430], 3)
    if frame == 0:
        pygame.draw.line(screen, SNOW, [537, 440], [547, 430], 3)
        pygame.draw.line(screen, BLACK, [552, 489], [559, 500], 3)
    if daytime == False:
        if frame == 0:
            pygame.draw.line(screen, SNOW, [537, 440], [547, 430], 3)
            pygame.draw.line(screen, YELLOW, [552, 489], [559, 500], 3)

    '''moving present'''

    pygame.draw.rect(screen, RED, [boxx, boxy, 10, 10])

    if left == True:
        boxx -= 6
    if right == True:
        boxx += 6        
    if up == True:
        boxy -= 6
    if down == True:
        boxy += 6     

    pygame.draw.line(screen, YELLOW, [ linex, liney], [linext, lineyt], 3)
    if left == True:
        linex -= 6
        linext -= 6
    if right == True:
        linex += 6
        linext += 6
    if up == True:
        liney -= 6
        lineyt -= 6
    if down == True:
        liney += 6
        lineyt += 6

    pygame.draw.line(screen, YELLOW, [horzx, horzy], [horzxt, horzyt], 3)
    
    if left == True:
        horzx -= 6
        horzxt -= 6
    if right == True:
        horzx += 6
        horzxt += 6
    if up == True:
        horzy -= 6
        horzyt -= 6
    if down == True:
        horzy += 6
        horzyt += 6

    '''draw snow and clouds'''

    for c in snow:
        draw_snow(c[0], c[1])
    for c in clouds:
        draw_cloud(c[0], c[1]) 

    

    ''' snow '''
    for c in snow:
        draw_snow(c[0], c[1])









    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
