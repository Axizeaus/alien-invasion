import pygame


class Ship:
    """A class to manage ship."""

    def __init__(self, ai_game):
        """Initializing the game and set it's staring position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it's rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        # update the ship's x values, not the rect
        # self.rect.right returns the right side of the rect of the ship
        # and self.rect.left returns left
        # the reason why the later is zero is because well, it's x,
        # x and y starts from top left corner and x is horizontal
        # which means x is either 0 or more in this case
        # self.screen_rect.right returns the end of screen's ride side, here it's 1200
        # because we made it 1200 * 800
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)