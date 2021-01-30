import pygame, sys, time, os, subprocess
from random import *
from pygame.locals import *

window_width = 720
window_height = 720

black = (0,0,0)
files_list = []

fps = 5
fps_clock = pygame.time.Clock()
pygame.init()

window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Snake')
font_obj = pygame.font.Font('freesansbold.ttf',20)

block_size = 40

class BLOCK():

    def __init__(self,coordinates):
        self.coordinates = coordinates
        self.head = False
        self.direction = None
        

block_array = [BLOCK((5,5)),BLOCK((4,5)),BLOCK((3,5))]

(block_array[0]).head = True

def draw(block_array):
    for block in block_array:
        #print(block_array.index(block),block.coordinates)
        
        x,y = block.coordinates
        x_dist,y_dist = (x * block_size),(y * block_size)
        rect = pygame.Rect(x_dist,y_dist,block_size,block_size)
        pygame.draw.rect(window,(255,255,255),rect,0)

    #print("DRAWING COMPLETE")

def random_food():
    
    present = True
    if len(block_array) != 19**2:
        while present == True:
            coordinate = (randint(0,10),randint(0,10))
            for block in block_array:
                if coordinate == block.coordinates:
                    present = True
                    break
            else:
                present = False
                
        return coordinate
    else:
        print("Game Over FROM RANDOM FOOD")
        game_over = True
        return (0,0)

def food_draw(coordinate):
    x,y = coordinate
    x_dist,y_dist = (x * block_size),(y * block_size)
    rect = pygame.Rect(x_dist,y_dist,block_size,block_size)
    pygame.draw.rect(window,(255,0,0),rect,0)

    print("Drawn food",coordinate)
    return coordinate

def text(score_text):
    #score_text = 'Score: ' + str(score)
    text_surface_obj = font_obj.render(score_text,True,(255,0,0))
    text_rect = text_surface_obj.get_rect()
    text_rect.center = (50,50)
    window.blit(text_surface_obj,text_rect)


move = None
game_over = False
new_head_pos = block_array[0].coordinates

food_pos = random_food()

started = False
score = 0
while True:
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            print (pygame.mouse.get_pos())
            
        if event.type == pygame.KEYDOWN:
            started = True
            
            if event.key == K_UP:
                move = "UP"
                
            elif event.key == K_DOWN:
                move = "DOWN"
                
            elif event.key == K_RIGHT:
                move = "RIGHT"
                
            elif event.key == K_LEFT:
                move = "LEFT"
        
    for i in range(len(block_array)-1,0,-1):
        if i != 0:
            block = block_array[i]
            block_array[i].coordinates = (block_array[i-1]).coordinates

    head = block_array[0]
    x,y = head.coordinates #retrieving coorinates of head segment
    if move == "UP" or head.direction == "UP":
        head.direction = "UP"
        new_head_pos = (x,y-1)
    if move == "DOWN" or head.direction == "DOWN":
        head.direction = "DOWN"
        new_head_pos = (x,y+1)
    if move == "RIGHT" or head.direction == "RIGHT":
        head.direction = "RIGHT"
        new_head_pos = (x+1,y)
    if move == "LEFT" or head.direction == "LEFT":
        head.direction = "LEFT"
        new_head_pos = (x-1,y)

    block_array[0].coordinates = new_head_pos

    if started:
        x,y = new_head_pos
        for i in range(1,len(block_array)):
            if new_head_pos == block_array[i].coordinates:
                game_over = True

        if x > 17 or x < 0:
            game_over = True
        if y > 17 or y <0:
            game_over = True

    if new_head_pos == food_pos:
        block_array.append(BLOCK(block_array[-1].coordinates))
        food_pos = random_food()
        score += 1

    if game_over == True:
        print("GAME OVER")
        time.sleep(10)
        pygame.quit()
        sys.exit()
        
        
    window.fill(black)
    draw(block_array)
    food_draw(food_pos)
    text(f"Score: {score}")
    
    
    
    pygame.display.update()
    fps_clock.tick(fps)

pygame.quit()
sys.exit()
