from cube import Cube
import moves


def white_cross(cube):
    # clear_top(cube)
    # Leaving the white face in the best position
    max = 0
    best = 0
    for i in range(4):
        c = check_white_edges(cube)
        if c > max:
            max = c
            best = i
        moves.move_step(cube, 'd', trace=False)
    for i in range(best):
        moves.move_step(cube, 'd')
    clear_top(cube)
    fix_botton_cross(cube)
    move_from_center(cube)
    flip_upper_edges(cube)


def check_white_edges(cube):
    buf = []
    count = 0
    # Checking number of white edges in white face
    if cube.colors[41] == 'w':
        buf.append(41)
    if cube.colors[44] == 'w':
        buf.append(44)
    if cube.colors[46] == 'w':
        buf.append(46)
    if cube.colors[43] == 'w':
        buf.append(43)
    for p in buf:
        if p == 41:
            other = cube.other_edge(p, 'w')
            if other[1] == 'r':
                count += 1
        if p == 44:
            other = cube.other_edge(p, 'w')
            if other[1] == 'g':
                count += 1
        if p == 46:
            other = cube.other_edge(p, 'w')
            if other[1] == 'o':
                count += 1
        if p == 43:
            other = cube.other_edge(p, 'w')
            if other[1] == 'b':
                count += 1
    return count

def fix_botton_cross(cube):
    if cube.colors[41] == 'w' and cube.colors[32] != 'r':
        moves.move(cube, 'f f')
        clear_top(cube)
    if cube.colors[43] == 'w' and cube.colors[29] != 'b':
        moves.move(cube, 'l l')
        clear_top(cube)
    if cube.colors[46] == 'w' and cube.colors[38] != 'o':
        moves.move(cube, 'b b')
        clear_top(cube)
    if cube.colors[44] == 'w' and cube.colors[35] != 'g':
        moves.move(cube, 'r r')
        clear_top(cube)

def flip_upper_edges(cube):
    if cube.colors[12] == 'w':
        if cube.colors[6] == 'b':
            moves.move(cube, 'f f f l')
            if cube.colors[24] == 'w':
                moves.move(cube, 'f')
        elif cube.colors[6] == 'g':
            moves.move(cube, 'f r r r') 
            if cube.colors[21] == 'w':
                moves.move(cube, 'f f f')
        elif cube.colors[6] == 'r':
            moves.move(cube, 'u u u r r r f')
            if cube.colors[26] == 'w':
                moves.move(cube, 'r')
        else:
            moves.move(cube, 'f f f r b b b')
            if cube.colors[23] == 'w':
                moves.move(cube, 'r r r')
        clear_top(cube)

def clear_top(cube):
    while cube.colors[1] == 'w' or cube.colors[4] == 'w' or cube.colors[6] == 'w' or cube.colors[3] == 'w':
        move_from_upper(cube)


def move_from_center(cube):
    if cube.colors[23] == 'w':
        moves.move(cube, 'r u')
        if cube.colors[23] == 'w':
            moves.move(cube, 'r r r ')
        clear_top(cube)
    if cube.colors[22] == 'w':
        moves.move(cube, 'l l l u')
        if cube.colors[22] == 'w':
            moves.move(cube, 'l')
        clear_top(cube)
    if cube.colors[21] == 'w':
        moves.move(cube, 'f u')
        if cube.colors[22] == 'w':
            moves.move(cube, 'f f f')
        clear_top(cube)
    if cube.colors[20] == 'w':
        moves.move(cube, 'b b b u')
        if cube.colors[20] == 'w':
            moves.move(cube, 'b')
        clear_top(cube)
    if cube.colors[27] == 'w':
        moves.move(cube, 'l u')
        if cube.colors[27] == 'w':
            moves.move(cube, 'l l l')
        clear_top(cube)
    if cube.colors[26] == 'w':
        moves.move(cube, 'r r r u')
        if cube.colors[26] == 'w':
            moves.move(cube, 'r')
        clear_top(cube)
    if cube.colors[25] == 'w':
        moves.move(cube, 'b u')
        if cube.colors[25] == 'w':
            moves.move(cube, 'b b b')
        clear_top(cube)
    if cube.colors[24] == 'w':
        moves.move(cube, 'f f f u')
        if cube.colors[24] == 'w':
            moves.move(cube, 'f')
        clear_top(cube)

def move_from_upper(cube):
    buf = []
    # Checking number of white edges in upper face
    if cube.colors[1] == 'w':
        buf.append(1)
    if cube.colors[4] == 'w':
        buf.append(4)
    if cube.colors[6] == 'w':
        buf.append(6)
    if cube.colors[3] == 'w':
        buf.append(3)

    for p in buf:
        other = cube.other_edge(buf[0], 'w')
        if other[1] == 'r':
            if p == 4:
                moves.move_step(cube, 'u')
            if p == 1:
                moves.move_step(cube, 'u')
                moves.move_step(cube, 'u')
            if p == 3:
                moves.move_step(cube, 'u')
                moves.move_step(cube, 'u')
                moves.move_step(cube, 'u')
            moves.move(cube, 'f f')
        if other[1] == 'g':
            if p == 1:
                moves.move_step(cube, 'u')
            if p == 3:
                moves.move_step(cube, 'u')
                moves.move_step(cube, 'u')
            if p == 6:
                moves.move_step(cube, 'u')
                moves.move_step(cube, 'u')
                moves.move_step(cube, 'u')
            moves.move(cube, 'r r')
        if other[1] == 'o':
            if p == 3:
                moves.move_step(cube, 'u')
            if p == 6:
                moves.move_step(cube, 'u')
                moves.move_step(cube, 'u')
            if p == 4:
                moves.move_step(cube, 'u')
                moves.move_step(cube, 'u')
                moves.move_step(cube, 'u')
            moves.move(cube, 'b b')
        if other[1] == 'b':
            if p == 6:
                moves.move_step(cube, 'u')
            if p == 4:
                moves.move_step(cube, 'u')
                moves.move_step(cube, 'u')
            if p == 1:
                moves.move_step(cube, 'u')
                moves.move_step(cube, 'u')
                moves.move_step(cube, 'u')
            moves.move(cube, 'l l')


def solve(cube):
    ''' if solved(cube):
        return '''
    white_cross(cube)
