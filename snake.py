import math
import random
import pygame 
import time


#initalize the pygame
pygame.init()

#variables for screen size

screen_width = 400
screen_height = 400


#displaying the screen
window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Snake Game!')

#initializing colors
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
brown = (165,42,42)

clock = pygame.time.Clock()
snake_speed = 15
snake_width = 10

#game_over = False

#x1 = screen_width/2
#y1 = screen_height/2

#x1_change = 0
#y1_change = 0

font_style = pygame.font.SysFont(None,30)
def your_score(score):
    value = font_style.render("Your Score: "+str(score),True,green)
    window.blit(value,[0,0])

def our_snake(snake_width,snake_list):
    for x in snake_list:
        pygame.draw.rect(window,red,[x[0],x[1],snake_width,snake_width])

def message(msg,color):
    msg = font_style.render(msg,True,color)
    window.blit(msg,[screen_width/4,screen_height/4])

def gameLoop():
    game_over = False
    game_close = False

    x1 = screen_width/2
    y1 = screen_height/2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, screen_width - snake_width) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_width - snake_width) / 10.0) * 10.0
    
    while not game_over:
        #CAteches all the events that has occured since the game has started (events-mouse movement and keypress)
        while game_close == True:
            window.fill(black)
            message("You Lost! Q-Quit or P-PLay",red)    
            pygame.display.update() 

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            #When you press the close window button
            if event.type == pygame.QUIT:
                game_over=True #loop breaks
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_width
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_width
                    y1_change = 0
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_width
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_width
        if x1 >= screen_width or x1<0 or y1<0 or y1 >=screen_height: #x1,y1<0-because (x1,y1)=(0,0) at top leftside
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window,green,[foodx,foody,snake_width,snake_width])
       
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        

        our_snake(snake_width,snake_list)
        your_score(length_of_snake-1)
        #pygame.draw.rect(window,red,[x1,y1,snake_width,snake_width]) #(x,y,width,height)
        pygame.display.update()

        if x1 == foodx and y1 == foody :
            foodx = round(random.randrange(0, screen_width - snake_width) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_width - snake_width) / 10.0) * 10.0
            length_of_snake += 1
        clock.tick(snake_speed)  


 
    pygame.quit()
    quit()

gameLoop()

