import cube
from random import randint

def move_right(cube):
    copy = list(cube.colors)
    copy[7] = cube.colors[33]
    copy[4] = cube.colors[23]
    copy[2] = cube.colors[13]
    copy[17] = cube.colors[7]
    copy[26] = cube.colors[4]
    copy[37] = cube.colors[2]
    copy[47] = cube.colors[17]
    copy[44] = cube.colors[26]
    copy[42] = cube.colors[37]
    copy[33] = cube.colors[47]
    copy[23] = cube.colors[44]
    copy[13] = cube.colors[42]

    copy[16] = cube.colors[14]
    copy[25] = cube.colors[15]
    copy[36] = cube.colors[16]
    copy[35] = cube.colors[25]
    copy[34] = cube.colors[36]
    copy[24] = cube.colors[35]
    copy[14] = cube.colors[34]
    copy[15] = cube.colors[24]
    cube.colors = copy

def move_left(cube):
    copy = list(cube.colors)
    copy[40] = cube.colors[11]
    copy[43] = cube.colors[22]
    copy[45] = cube.colors[31]
    copy[39] = cube.colors[40]
    copy[27] = cube.colors[43]
    copy[19] = cube.colors[45]
    copy[0] = cube.colors[39]
    copy[3] = cube.colors[27]
    copy[5] = cube.colors[19]
    copy[11] = cube.colors[0]
    copy[22] = cube.colors[3]
    copy[31] = cube.colors[5]
    
    copy[10] = cube.colors[8]
    copy[21] = cube.colors[9]
    copy[30] = cube.colors[10]
    copy[29] = cube.colors[21]
    copy[28] = cube.colors[30]
    copy[20] = cube.colors[29]
    copy[8] = cube.colors[28]
    copy[9] = cube.colors[20]
    cube.colors = copy

def move_top(cube):
    copy = list(cube.colors)
    copy[8] = cube.colors[11]
    copy[9] = cube.colors[12]
    copy[10] = cube.colors[13]
    copy[11] = cube.colors[14]
    copy[12] = cube.colors[15]
    copy[13] = cube.colors[16]
    copy[14] = cube.colors[17]
    copy[15] = cube.colors[18]
    copy[16] = cube.colors[19]
    copy[17] = cube.colors[8]
    copy[18] = cube.colors[9]
    copy[19] = cube.colors[10]
    
    copy[0] = cube.colors[5]
    copy[1] = cube.colors[3]
    copy[2] = cube.colors[0]
    copy[4] = cube.colors[1]
    copy[7] = cube.colors[2]
    copy[6] = cube.colors[4]
    copy[5] = cube.colors[7]
    copy[3] = cube.colors[6]
    cube.colors = copy

def move_down(cube):
    copy = list(cube.colors)
    copy[28] = cube.colors[37]
    copy[29] = cube.colors[38]
    copy[30] = cube.colors[39]
    copy[31] = cube.colors[28]
    copy[32] = cube.colors[29]
    copy[33] = cube.colors[30]
    copy[34] = cube.colors[31]
    copy[35] = cube.colors[32]
    copy[36] = cube.colors[33]
    copy[37] = cube.colors[34]
    copy[38] = cube.colors[35]
    copy[39] = cube.colors[36]
    
    copy[40] = cube.colors[45]
    copy[41] = cube.colors[43]
    copy[42] = cube.colors[40]
    copy[44] = cube.colors[41]
    copy[47] = cube.colors[42]
    copy[46] = cube.colors[44]
    copy[45] = cube.colors[47]
    copy[43] = cube.colors[46]
    cube.colors = copy

def move_front(cube):
    copy = list(cube.colors)
    copy[5] = cube.colors[30]
    copy[6] = cube.colors[21]
    copy[7] = cube.colors[10]
    copy[14] = cube.colors[5]
    copy[24] = cube.colors[6]
    copy[34] = cube.colors[7]
    copy[42] = cube.colors[14]
    copy[41] = cube.colors[24]
    copy[40] = cube.colors[34]
    copy[30] = cube.colors[42]
    copy[21] = cube.colors[41]
    copy[10] = cube.colors[40]
    
    copy[11] = cube.colors[31]
    copy[12] = cube.colors[22]
    copy[13] = cube.colors[11]
    copy[23] = cube.colors[12]
    copy[33] = cube.colors[13]
    copy[32] = cube.colors[23]
    copy[31] = cube.colors[33]
    copy[22] = cube.colors[32]
    cube.colors = copy

def move_back(cube):
    copy = list(cube.colors)
    copy[16] = cube.colors[47]
    copy[25] = cube.colors[46]
    copy[36] = cube.colors[45]
    copy[2] = cube.colors[36]
    copy[1] = cube.colors[25]
    copy[0] = cube.colors[16]
    copy[8] = cube.colors[2]
    copy[20] = cube.colors[1]
    copy[28] = cube.colors[0]
    copy[45] = cube.colors[8]
    copy[46] = cube.colors[20]
    copy[47] = cube.colors[28]
    
    copy[17] = cube.colors[37]
    copy[18] = cube.colors[26]
    copy[19] = cube.colors[17]
    copy[27] = cube.colors[18]
    copy[39] = cube.colors[19]
    copy[38] = cube.colors[27]
    copy[37] = cube.colors[39]
    copy[26] = cube.colors[38]
    cube.colors = copy

def move_step(cube, direction, trace=True):
    if direction is 'r':
        move_right(cube)
    elif direction is 'l':
        move_left(cube)
    elif direction is 'u':
        move_top(cube) 
    elif direction is 'f':
        move_front(cube)
    elif direction is 'b':
        move_back(cube)
    elif direction is 'd':
        move_down(cube)
    else:
        return
    if trace:
        cube.solution += direction + ' '

def move(cube, movements, trace=True):
    mov = movements.split(' ')
    for m in mov:
        move_step(cube, m, trace)

def scramble(cube, n):
    scramble = ''
    mov = ['r', 'l', 'u', 'f', 'b', 'd']
    for i in range(n):
        rand = randint(0, 5)
        scramble += mov[rand] + ' '
    move(cube, scramble, False)
    return scramble