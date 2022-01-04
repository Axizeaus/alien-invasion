import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullets
from alien import Alien
from game_stats import GameStats


class AlienInvasion(object):
    """Main code to control game flow."""

    def __init__(self):
        """Initializing the game."""
        pygame.init()
        self.settings = Settings()

        # Create an instance to store game statics
        self.stats = GameStats(self)

        # making a full screen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # making that little line on the game window
        pygame.display.set_caption("Alien Invasion version 1.0")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Running and quitting the game"""
        while True:
            self.ship.update()
            # checking the input ( keyboard and mouse )
            self._check_events()
            # redraw the screen during each pass of the loop
            self._update_screen()
            self._update_bullets()
            self._update_aliens()

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
        self.aliens.draw(self.screen)
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
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet alien collisions"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Create an alien and find the number of alien in a row
        # spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                # Create an alien and place it in a row
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in a row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (2 * alien_width * alien_number)
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """
        Check if the fleet is at the edge and then
        Update the position of all aliens of a fleet
        """
        self.aliens.update()
        self.check_fleet_edges()

        # look for alien ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def check_fleet_edges(self):
        """Responds appropriately if any alien reaches the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Responds to the ship being hit by alien"""

        # decrease the ship left
        self.stats.ship_left -= 1

        # Get rid of any remaining aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        # pause
        sleep(0.5)


if __name__ == '__main__':
    # make an instance of the class AlienInvasion() and running it
    ai = AlienInvasion()
    ai.run_game()
