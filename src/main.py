from turtle import width
import pygame, sys
from settings import *
from debug import debug
from level import Level

class Game:
    # Initialize pygame window
    def __init__(self) :
        
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('python-game')
        self.clock = pygame.time.Clock()

        # getting level information
        self.level = Level()

    # Running ingame content
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

# Running Game class
if __name__ == '__main__':
    game = Game()
    game.run()