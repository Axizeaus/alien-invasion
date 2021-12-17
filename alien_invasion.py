import sys

import pygame


def run_game():
    """Running and quitting the game"""
    while True:
        # checking the input ( keyboard and mouse )
        for event in pygame.event.get():
            # if quit then quit
            if event.type == pygame.QUIT:
                sys.exit()

        # making the recent screen visible
        pygame.display.flip()


class AlienInvasion(object):
    """Main code to control game flow."""

    def __init__(self):

        """Initializing the game."""
        pygame.init()

        # making a screen with 1200, 800
        self.screen = pygame.display.set_mode((1200, 800))
        # making that little line on the game window
        pygame.display.set_caption("Alien Invasion version 1.0")


if __name__ == '__main__':
    # make an instance of the class AlienInvasion() and running it
    ai = AlienInvasion()
    run_game()
