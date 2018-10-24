from mods.cube import Cube
import mods.draw as draw
import mods.moves as moves
import os
import pygame
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = BASE_DIR + '/data/'
TEMPLATE_DIR = DATA_DIR + '/templates/'

REST_FILENAME = os.path.join(DATA_DIR, 'restrictions.json')
COLOR_FILENAME = os.path.join(TEMPLATE_DIR, 'solved.dat')

cube = Cube(REST_FILENAME, COLOR_FILENAME)

pygame.init()
screen = pygame.display.set_mode((750, 600))
screen.fill((255, 255, 255))

moves.scramble(cube, 10)
# moves.move(cube, "b u d r d l f u r r")

draw.paint_cube(cube, screen)

while True:
    pygame.display.update()
    inp = raw_input("Movement: ")
    moves.move_step(cube, inp)
    draw.paint_cube(cube, screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()