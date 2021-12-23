import sys
import pygame

from settings import Settings
from ship import Ship


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
        self.ship = Ship(self)

    def run_game(self):
        """Running and quitting the game"""
        while True:
            # checking the input ( keyboard and mouse )
            self._check_events()
            # redraw the screen during each pass of the loop
            self._update_screen()
            self.ship.update()

    def _check_events(self):
        """Respond the keyboard and mouse movement"""
        for event in pygame.event.get():
            # if quit then quit
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # move the ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # move the ship to the left
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                # stop the movement
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _update_screen(self):
        """Update images on the screen and flip to a new screen"""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    # make an instance of the class AlienInvasion() and running it
    ai = AlienInvasion()
    ai.run_game()
