import json
import logging
import moves

LOG_FILENAME = 'rubik_solver.log'

logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s[%(filename)s:%(lineno)d] %(message)s', datefmt='%d-%m-%Y:%H:%M:%S', filename=LOG_FILENAME)

class Cube:
    def __init__(self, file_restrictions, file_colors):
        with open(file_restrictions, "r") as f:
            restrictions = json.load(f)

        # Creating the structure of the cube
        if "corners" not in restrictions or "edges" not in restrictions:
            logging.error('Invalid syntax on '+ file_restrictions)
            return
        
        # A corner is a list of 3 postitions
        self.corners = restrictions['corners']
        # An edge is a list of 2 positions
        self.edges = restrictions['edges']
        # neighbors is a dictionary to map each index with its piece
        self.neighbors = {}

        for corner in self.corners:
            for index in corner:
                self.neighbors[index] = corner

        for edge in self.edges:
            for index in edge:
                self.neighbors[index] = edge

        # "Painting" the cube
        self.colors = []
        with open(file_colors, 'r') as f:
            for line in f:
                self.colors += line.split(' ')
            self.colors = [color for color in self.colors if color not in ['', '\n']]





