import pygame

from settings import *

#_ is empty space, 1 is wall

_ = False

minimap = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
           [1, _, _, 1, 1, 1, 1, _, _, 1, 1, 1, _, _, _, 1],
           [1, _, _, _, _, _, 1, _, _, _, 1, _, _, _, _, 1],
           [1, _, _, _, _, _, 1, _, _, _, 1, _, _, _, _, 1],
           [1, _, 1, 1, 1, 1, 1, _, _, _, 1, 1, _, _, _, 1],
           [1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, 1],
           [1, _, _, _, 1, _, _, _, 1, 1, _, _, _, _, _, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
           ]

class Map:

    def __init__(self, game):

        self.game = game
        self.minimap = minimap
        self.worldmap = {}
        self.get_map()

    def get_map(self):
        #it adds to the worldmap dictionary every wall tile
        for j, row in enumerate(self.minimap):
            for i, value in enumerate(row):
                if value:
                    self.worldmap[(i, j)] = value

    def draw_map(self):
        #draws the walls as empty squares 
        for position in self.worldmap:
            pygame.draw.rect(self.game.screen, 'darkgrey', (position[0] * tile_size, position[1] * tile_size, tile_size, tile_size), 2) 
        