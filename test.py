import pygame
import os
import time
import random

pygame.init()

WIDTH = 750
HEIGHT = 750

screen = pygame.display
screen.set_mode((720,480))
#pygame.display.set_caption("Last Space")

running = True
while running: # This would start the event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # This would be a quit event.
            running = False # So the user can close the program
    screen.fill(0,0,0) # This fills the screen with black colour.
    pygame.display.flip() # This "flips" the display so that it shows something
pygame.quit()
