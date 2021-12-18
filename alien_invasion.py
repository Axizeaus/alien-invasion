import sys

import pygame
from settings import Settings


class AlienInvasion(object):
    """Main code to control game flow."""

    def __init__(self):
        """Initializing the game."""
        pygame.init()
        self.settings = Settings()

        # making a screen with 1200, 800
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # making that little line on the game window
        pygame.display.set_caption("Alien Invasion version 1.0")

    def run_game(self):
        """Running and quitting the game"""
        while True:
            # checking the input ( keyboard and mouse )
            for event in pygame.event.get():
                # if quit then quit
                if event.type == pygame.QUIT:
                    sys.exit()
            # redraw the screen during each pass of the loop
            self.screen.fill(self.settings.bg_colour)

            # making the recent screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # make an instance of the class AlienInvasion() and running it
    ai = AlienInvasion()
    ai.run_game()
