'''
Program Name: Alien Invasion
Author: Henoc Cherestal
Purpose: Define the Bullet class for the Alien Invasion game.
Starter Code: Based on the Alien Invasion project from class and
Python Crash Course, 3rd Edition by Eric Matthes.
Date: 04/14/2026
'''

import pygame
from pygame.sprite import Sprite

from settings import Settings


class Bullet(Sprite):
    '''Manage bullets fired from the player's ship.'''

    def __init__(self, ai_game) -> None:
        '''Create a bullet object at the ship's current position.'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings: Settings = ai_game.settings

        self.rect = pygame.Rect(
            0,
            0,
            self.settings.bullet_width,
            self.settings.bullet_height,
        )
        self.rect.midbottom = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)