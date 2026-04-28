'''
Program Name: Alien Invasion
Author: Henoc Cherestal
Purpose: Track game statistics for Alien Invasion.
Starter Code: Based on the Alien Invasion project from class and
Python Crash Course, 3rd Edition by Eric Matthes.
Date: 04/28/2026
'''


class GameStats:
    '''for tracking statistics for Alien Invasion.'''

    def __init__(self, ai_game) -> None:
        '''Initializing the game statistics.'''
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self) -> None:
        '''Reset statistics that can change during the game.'''
        self.ships_left = self.settings.ships_limit
        self.score = 0
        self.level = 1