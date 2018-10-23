def parse_colors(file):
    colors = []
    with open(file, 'r') as f:
        for line in f:
            colors += line.split(' ')
        colors = [color for color in colors if color not in ['', '\n']]
    print(colors)
            
                

parse_colors('colours.dat')