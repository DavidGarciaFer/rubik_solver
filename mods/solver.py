from cube import Cube
import moves


def white_cross(cube):
    # clear_top(cube)
    # Leaving the white face in the best position
    max = 0
    best = 0
    flag = 0
    for i in range(4):
        c = check_white_edges(cube)
        if c > max:
            max = c
            best = i
        moves.move_step(cube, 'd', trace=False)
    for i in range(best):
        moves.move_step(cube, 'd')

    while check_white_cross(cube) == False:
        if cube.colors[1] == 'w' or cube.colors[6] == 'w' or cube.colors[4] == 'w' or cube.colors[3] == 'w':
            clear_top(cube)
        fix_botton_cross(cube)
        for i in range(20, 28):
            if cube.colors[i] == 'w':
                flag = 1
        if flag == 1:
            move_from_center(cube)
            flag = 0
        if cube.colors[9] == 'w' or cube.colors[12] == 'w' or cube.colors[15] == 'w' or cube.colors[18] == 'w':
            flip_upper_edges(cube)
        send_edge_from_bottom(cube)


def check_white_cross(cube):
    return cube.colors[41] == 'w' and cube.colors[43] == 'w' \
        and cube.colors[46] == 'w' and cube.colors[44] == 'w' \
        and cube.colors[32] == 'r' and cube.colors[35] == 'g' \
        and cube.colors[38] == 'o' and cube.colors[29] == 'b'


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
    if cube.colors[9] == 'w':
        moves.move(cube, 'u u u')
    elif cube.colors[18] == 'w':
        moves.move(cube, 'u u')
    elif cube.colors[15] == 'w':
        moves.move(cube, 'u')
    elif cube.colors[12] != 'w':
        return
    flip_upper_edge(cube)


def flip_upper_edge(cube):
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


def send_edge_from_bottom(cube):
    if cube.colors[29] == 'w':
        moves.move(cube, 'l l u u u')
        flip_upper_edge(cube)
    if cube.colors[32] == 'w':
        moves.move(cube, 'f f')
        flip_upper_edge(cube)
    if cube.colors[35] == 'w':
        moves.move(cube, 'r r u')
        flip_upper_edge(cube)
    if cube.colors[38] == 'w':
        moves.move(cube, 'b b u u')
        flip_upper_edge(cube)


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


def white_corners(cube):
    while (check_white_corners(cube) == False):
        top_corners(cube)
        top_corner_top(cube)
        fix_bottom_corners(cube)


def check_white_corners(cube):
    return cube.colors[40] == 'w' and cube.colors[42] == 'w' and \
        cube.colors[45] == 'w' and cube.colors[47] == 'w' and \
        cube.colors[31] == 'r' and cube.colors[28] == 'b' and \
        cube.colors[37] == 'o' and cube.colors[34] == 'g'


def fix_bottom_corners(cube):
    fix_bottom_corners_down(cube)
    fix_bottom_corners_front(cube)


def fix_bottom_corners_down(cube):
    if cube.colors[40] == 'w' and cube.colors[31] != 'r':
        moves.move(cube, 'f u f f f')
        top_corners(cube)
    if cube.colors[45] == 'w' and cube.colors[28] != 'b':
        moves.move(cube, 'b b b u b')
        top_corners(cube)
    if cube.colors[47] == 'w' and cube.colors[37] != 'o':
        moves.move(cube, 'b u b b b')
        top_corners(cube)
    if cube.colors[42] == 'w' and cube.colors[34] != 'g':
        moves.move(cube, 'r u r r r')
        top_corners(cube)


def fix_bottom_corners_front(cube):
    if cube.colors[33] == 'w':
        moves.move(cube, 'r u u u r r r')
        top_corners(cube)
    if cube.colors[30] == 'w':
        moves.move(cube, 'f u u u f f f')
        top_corners(cube)
    if cube.colors[39] == 'w':
        moves.move(cube, 'l u u u l l l')
        top_corners(cube)
    if cube.colors[36] == 'w':
        moves.move(cube, 'b u u u b b b')
        top_corners(cube)
    if cube.colors[31] == 'w':
        moves.move(cube, 'f u f f f')
        top_corners(cube)
    if cube.colors[28] == 'w':
        moves.move(cube, 'l u l l l')
        top_corners(cube)
    if cube.colors[37] == 'w':
        moves.move(cube, 'b u b b b')
        top_corners(cube)
    if cube.colors[34] == 'w':
        moves.move('r u r r r')
        top_corners(cube)


def top_corner_right(cube):
    if cube.colors[13] == 'w':
        if cube.colors[7] == 'r':
            moves.move(cube, 'u r u u u r r r')
        elif cube.colors[7] == 'b':
            moves.move(cube, 'u u f u u u f f f')
        elif cube.colors[7] == 'o':
            moves.move(cube, 'u u u l u u u l l l')
        else:
            moves.move(cube, 'b u u u b b b')


def top_corner_left(cube):
    if cube.colors[11] == 'w':
        if cube.colors[5] == 'r':
            moves.move(cube, 'u u u l l l u l')
        elif cube.colors[5] == 'g':
            moves.move(cube, 'u u f f f u f')
        elif cube.colors[5] == 'o':
            moves.move(cube, 'u r r r u r')
        else:
            moves.move(cube, 'b b b u b')


def top_corner_top(cube):
    if cube.colors[2] == 'w':
        moves.move(cube, 'u')
    elif cube.colors[0] == 'w':
        moves.move(cube, 'u u')
    elif cube.colors[5] == 'w':
        moves.move(cube, 'u u u')
    elif cube.colors[7] != 'w':
        return
    moves.move(cube, 'r u u r r r')
    top_corners(cube)


def top_corners(cube):
    while cube.colors[10] == 'w' or cube.colors[13] == 'w' or cube.colors[16] == 'w' or cube.colors[19] == 'w':
        if cube.colors[10] == 'w':
            moves.move(cube, 'u u u')
        elif cube.colors[19] == 'w':
            moves.move(cube, 'u u')
        elif cube.colors[16] == 'w':
            moves.move(cube, 'u')
        top_corner_right(cube)
    while cube.colors[8] == 'w' or cube.colors[11] == 'w' or cube.colors[14] == 'w' or cube.colors[17] == 'w':
        if cube.colors[8] == 'w':
            moves.move(cube, 'u u u')
        elif cube.colors[17] == 'w':
            moves.move(cube, 'u u')
        elif cube.colors[14] == 'w':
            moves.move(cube, 'u')
        top_corner_left(cube)

def mid_edges(cube):
    pass

def mid_edges_from_top(cube):
    pass

def solve(cube):
    white_cross(cube)
    top_corner_left(cube)
    white_corners(cube)
