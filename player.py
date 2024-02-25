import pygame
import math

from settings import *

class Player:

    def __init__(self, game):

        self.game = game
        self.x, self.y = player_pos
        self.angle = player_angle

    def move(self): #delta time is needed to make the movement speed independent of the framerate

        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        dx, dy = 0, 0

        speed = player_speed * self.game.delta_time
        speed_cos = speed * cos_a
        speed_sin = speed * sin_a

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pygame.K_d]:
            dx += -speed_sin
            dy += speed_cos          

        self.check_wall_coll(dx, dy)

        if keys[pygame.K_LEFT]:
            self.angle -= player_rotation_speed * self.game.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += player_rotation_speed * self.game.delta_time   

        self.angle %= math.tau #tau = 2*pi (used to normalize angle range)

    def check_if_wall(self, x, y):
        return (x, y) not in self.game.map.worldmap
        
    def check_wall_coll(self, dx, dy): #behaving weird. fix
        if  self.check_if_wall((int(self.x + dx)), int(self.y)):
                self.x += dx 
        if  self.check_if_wall(int(self.x), int(self.y + dy)):
                self.y += dy

    def draw_player(self):
        '''
        pygame.draw.line(self.game.screen, 'yellow', (self.x * tile_size, self.y * tile_size), 
                         ((self.x * tile_size + width * math.cos(self.angle)),
                         (self.y * tile_size + width * math.sin (self.angle))), 2)   
        ''' 

        pygame.draw.circle(self.game.screen, 'red', (self.x * tile_size, self.y * tile_size), 15)
    
    def update(self):
        self.move()

    @property
    def pos(self): #players coords
        return self.x, self.y    
    
    @property
    def map_pos(self): #integer coords to know which tile on map player is
        return int(self.x), int(self.y)