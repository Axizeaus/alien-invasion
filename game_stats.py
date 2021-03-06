class GameStats:
    """Track statics for the game"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start alien invasion in inactive state
        self.game_active = False

        # high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """initialize statics that can change during the game"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
