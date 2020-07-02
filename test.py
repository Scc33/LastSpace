import pygame
import os
import time
import random

pygame.init()

WIDTH = 750
HEIGHT = 750

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Last Space")

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

def redraw_window():
    WIN.blit(BACKGROUND, (0,0))

while True:
    redraw_window()
