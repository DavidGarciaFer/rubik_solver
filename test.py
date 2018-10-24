from mods.cube import Cube
import mods.draw as draw
import mods.moves as moves
import mods.solver as solver
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

#scramble = moves.scramble(cube, 10)
#print scramble
#moves.move(cube, "f r u b b d r l u r l")
#moves.move(cube, "l b l b d f l r l l")
moves.move(cube, "d u f d r d f u b b")

draw.paint_cube(cube, screen)
pygame.display.update()
inp = raw_input("Solve: ")
solver.solve(cube)
draw.paint_cube(cube, screen)

while True:
    pygame.display.update()
    inp = raw_input("Movement: ")
    if inp == 'q':
        pygame.quit()
        sys.exit()
    moves.move_step(cube, inp)
    draw.paint_cube(cube, screen)
    print('Movements history: '+ cube.solution)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
