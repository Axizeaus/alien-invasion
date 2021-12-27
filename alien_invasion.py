import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullets


class AlienInvasion(object):
    """Main code to control game flow."""

    def __init__(self):
        """Initializing the game."""
        pygame.init()
        self.settings = Settings()

        # making a full screen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # making that little line on the game window
        pygame.display.set_caption("Alien Invasion version 1.0")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Running and quitting the game"""
        while True:
            # checking the input ( keyboard and mouse )
            self._check_events()
            # redraw the screen during each pass of the loop
            self._update_screen()
            self._update_bullets()
            self.ship.update()



    def _check_events(self):
        """Respond the keyboard and mouse movement"""
        for event in pygame.event.get():
            # if quit then quit
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responds to key down events"""
        if event.key == pygame.K_RIGHT:
            # move the ship to the right
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            # move the ship to the left
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            # quit the game when pressed q
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self, event):
        """Responds to key up events"""
        # stop the movement
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullets(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullets = Bullets(self)
            self.bullets.add(new_bullets)

    def _update_screen(self):
        """Update images on the screen and flip to a new screen"""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        for bullets in self.bullets.sprites():
            bullets.draw_bullet()
        pygame.display.flip()

    def _update_bullets(self):
        """update position of bullets and get rid of old bullets"""
        self.bullets.update()
        # get rid of the bullets once they disappear from the window
        # reason why : because those bullets just disappear from the view but
        # they still exists which is taking up memory and processing power
        # so in the long run, that'll cause problems
        for bullets in self.bullets.copy():
            if bullets.rect.bottom <= 0:
                self.bullets.remove(bullets)


if __name__ == '__main__':
    # make an instance of the class AlienInvasion() and running it
    ai = AlienInvasion()
    ai.run_game()
