import pygame
import character_list, mechanics

pygame.init()

screen = pygame.display.set_mode()
x, y = screen.get_size()
pygame.display.set_mode((x, y)) 

isGameRunning = True

while isGameRunning:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           isGameRunning = False