'''
Program Name: Alien Invasion
Author: Henoc Cherestal
Purpose: Store the settings for the Alien Invasion game.
Starter Code: Based on the Alien Invasion project from class and
Python Crash Course, 3rd Edition by Eric Matthes.
Date: 04/14/2026
'''

from pathlib import Path

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

        self.ship_width = 110
        self.ship_height = 110
        self.bullet_width = 24
        self.bullet_height = 60 

        self.alien_width = 88
        self.alien_height = 88
        self.alien_speed = 1.5
        self.fleet_drop_speed = 18
        self.fleet_direction = 1

        self.base_dir = Path(__file__).resolve().parent
        self.assets_dir = self.base_dir / "Assets"
        self.images_dir = self.assets_dir / "images"

        self.ship_image = self.images_dir / "ship.png"
        self.bullet_image = self.images_dir / "laserBlast.png"
        self.background_image = self.images_dir / "Starbasesnow.png"
        self.alien_image = self.images_dir / "alien.png"