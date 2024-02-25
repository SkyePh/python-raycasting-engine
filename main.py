import pygame
import sys

from settings import *
from map import Map
from player import Player
from raycasting import Raycasting

class Main:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.delta_time = 1

        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = Raycasting(self)

    def update_screen(self):

        self.player.update()
        self.raycasting.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(fps)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):

        self.screen.fill('black')   
        #self.map.draw_map() 
        #self.player.draw_player()

    def check_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def mainloop(self):

        while True:
            self.check_events()
            self.update_screen()
            self.draw()   

if __name__ == '__main__':
    game = Main()
    game.mainloop()            
