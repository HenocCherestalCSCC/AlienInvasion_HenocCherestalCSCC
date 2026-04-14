'''
Program Name: Alien Invasion
Author: Henoc Cherestal
Purpose: Store the settings for the Alien Invasion game.
Starter Code: Based on the Alien Invasion project from class and
Python Crash Course, 3rd Edition by Eric Matthes.
Date: 04/14/2026
'''


class Settings:
    '''Store all settings for the Alien Invasion game.'''

    def __init__(self) -> None:
        '''Initialize the game's main screen settings.'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 10, 25)
        self.caption = "Alien Invasion"