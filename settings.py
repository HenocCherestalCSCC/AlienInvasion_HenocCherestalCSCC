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

        self.ship_speed = 5.0
        self.bullet_speed = 8.0
        self.bullets_allowed = 5
        self.fps = 60

        self.ship_width = 80
        self.ship_height = 48
        self.ship_color = (100, 220, 255)

        self.bullet_width = 6
        self.bullet_height = 18
        self.bullet_color = (255, 80, 80)