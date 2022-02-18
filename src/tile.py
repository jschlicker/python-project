from lib2to3.pytree import convert
import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    
    # Initialize tile
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('../assets/environment/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)