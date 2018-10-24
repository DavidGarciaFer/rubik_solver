from cube import Cube
import moves


def white_cross(cube):
    # clear_top(cube)
    buf = []
    # Checking number of white edges in white face
    if cube.colors[41] == 'w':
        buf.append(41)
    if cube.colors[44] == 'w':
        buf.append(44)
    if cube.colors[46] == 'w':
        buf.append(46)
    if cube.colors[43] == 'w':
        buf.append(43)

    if len(buf) == 1:
        # Placing the piece in its gap
        other = cube.other_edge(buf[0], 'w')
        if other[1] == 'r' and other[0] != 32:
            if other[0] == 29:
                moves.move_step(cube, 'd')
            elif other[0] == 38:
                moves.move_step(cube, 'd')
                moves.move_step(cube, 'd')
            else:
                moves.move_step(cube, 'd')
                moves.move_step(cube, 'd')
                moves.move_step(cube, 'd')
        if other[1] == 'b' and other[0] != 29:
            if other[0] is 38:
                moves.move_step(cube, 'd')
            elif other[0] == 35:
                moves.move_step(cube, 'd')
                moves.move_step(cube, 'd')
            else:
                moves.move_step(cube, 'd')
                moves.move_step(cube, 'd')
                moves.move_step(cube, 'd')
        if other[1] == 'o' and other[0] != 38:
            if other[0] == 35:
                moves.move_step(cube, 'd')
            elif other[0] == 32:
                moves.move_step(cube, 'd')
                moves.move_step(cube, 'd')
            else:
                moves.move_step(cube, 'd')
                moves.move_step(cube, 'd')
                moves.move_step(cube, 'd')
        if other[1] is 'g' and other[0] is not 35:
            if other[0] == 32:
                moves.move_step(cube, 'd')
            elif other[0] == 29:
                moves.move_step(cube, 'd')
                moves.move_step(cube, 'd')
            else:
                moves.move_step(cube, 'd')
                moves.move_step(cube, 'd')
                moves.move_step(cube, 'd')

    elif len(buf) > 1:
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


def clear_top(cube):
    while cube.colors[1] == 'w' or cube.colors[4] == 'w' or cube.colors[6] == 'w' or cube.colors[3] == 'w':
        move_from_upper(cube)


def move_from_center(cube):
    pass


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
