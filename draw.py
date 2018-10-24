import pygame # pylint: disable=import-error
import sys
from cube import Cube
import moves

red = (255, 0, 0)
blue = (0, 76, 153)
yellow = (255, 255, 0)
orange = (255, 128, 0)
green = (0, 153, 0)
white = (255, 255, 255)
black = (0, 0, 0)

def g_color(color):
    if color is 'r':
        return red
    elif color is 'b':
        return blue
    elif color is 'y':
        return  yellow
    elif color is 'o':
        return orange
    elif color is 'g':
        return green
    else:
        return white

REST_FILENAME = 'restrictions.json'
COLOR_FILENAME = 'colors.dat'

width = 750
height = 600
face_size = 150
piece_size = face_size/3
offset = face_size/2
border = 3

cube = Cube(REST_FILENAME, COLOR_FILENAME)
# moves.move_right(cube)
# moves.move_right(cube)
# moves.move_left(cube)
# moves.move_left(cube)
# moves.move_top(cube)
# moves.move_top(cube)
# moves.move_down(cube)
# moves.move_down(cube)
# moves.move_front(cube)
# moves.move_front(cube)
# moves.move_back(cube)
# moves.move_back(cube)

pygame.init()

screen = pygame.display.set_mode((width, height))
screen.fill(white)

# Filling upper side
counter = 0
for j in range(3):
    for i in range(3):
        if i == 1 and j == 1:
            screen.fill(yellow, rect=[offset+face_size+piece_size, offset+piece_size, 50, 50])
        else:
            screen.fill(g_color(cube.colors[counter]), rect=[offset+face_size+piece_size*i, offset+piece_size*j, 50, 50])
            counter += 1

# Filling middle part
for j in range(3):
    for i in range(12):
        if i == 1 and j == 1:
            screen.fill(blue, rect=[offset+piece_size, offset+face_size+piece_size, 50, 50])
        elif i == 4 and j == 1:
            screen.fill(red, rect=[offset+piece_size*4, offset+face_size+piece_size, 50, 50])
        elif i == 7 and j == 1:
            screen.fill(green, rect=[offset+piece_size*7, offset+face_size+piece_size, 50, 50])
        elif i == 10 and j == 1:
            screen.fill(orange, rect=[offset+piece_size*10, offset+face_size+piece_size, 50, 50])
        else:
            screen.fill(g_color(cube.colors[counter]), rect=[offset+piece_size*i, offset+face_size+piece_size*j, 50, 50])
            counter += 1

# Filling bottom
for j in range(3):
    for i in range(3):
        if i == 1 and j == 1:
            screen.fill(white, rect=[offset+face_size+piece_size, offset+face_size*2+piece_size, 50, 50])
        else:
            screen.fill(g_color(cube.colors[counter]), rect=[offset+face_size+piece_size*i, offset+face_size*2+piece_size*j, 50, 50])
            counter += 1

# Upper side
pygame.draw.rect(screen, black, (offset+face_size, offset, face_size, face_size), border)
# Left side
pygame.draw.rect(screen, black, (offset, offset+face_size, face_size, face_size), border)
# Front side
pygame.draw.rect(screen, black, (offset+face_size, offset+face_size, face_size, face_size), border)
# Right side
pygame.draw.rect(screen, black, (offset+face_size*2, offset+face_size, face_size, face_size), border)
# Back side
pygame.draw.rect(screen, black, (offset+face_size*3, offset+face_size, face_size, face_size), border)
# Front side
pygame.draw.rect(screen, black, (offset+face_size, offset+face_size*2, face_size, face_size), border)

# Upper side grid
for i in range(3):
    for j in range(3):
        pygame.draw.rect(screen, black, (offset+face_size+piece_size*i, offset+piece_size*j, piece_size, piece_size), border - 1)

# Left side grid
for i in range(3):
    for j in range(3):
        pygame.draw.rect(screen, black, (offset+piece_size*i, face_size+offset+piece_size*j, piece_size, piece_size), border - 1)

# Front side grid
for i in range(3):
    for j in range(3):
        pygame.draw.rect(screen, black, (offset+face_size+piece_size*i, offset+face_size+piece_size*j, piece_size, piece_size), border - 1)

# Right side grid
for i in range(3):
    for j in range(3):
        pygame.draw.rect(screen, black, (offset+face_size*2+piece_size*i, offset+face_size+piece_size*j, piece_size, piece_size), border - 1)

# Back side grid
for i in range(3):
    for j in range(3):
        pygame.draw.rect(screen, black, (offset+face_size*3+piece_size*i, offset+face_size+piece_size*j, piece_size, piece_size), border - 1)

# Bottom side grid
for i in range(3):
    for j in range(3):
        pygame.draw.rect(screen, black, (offset+face_size+piece_size*i, offset+face_size*2+piece_size*j, piece_size, piece_size), border - 1)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();