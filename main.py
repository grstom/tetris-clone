import pygame
from game import Tetris


screen_width, screen_height = 600,600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

pygame.init()

tetris = Tetris(screen)

tetris.CreateBlocks(screen_width, screen_height)

tetris.createTetriminos()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    # tetris.checkBlocks()
    
    tetris.moveBlocks()

    tetris.drawBlocks()

    clock.tick(20)
    pygame.display.update()

