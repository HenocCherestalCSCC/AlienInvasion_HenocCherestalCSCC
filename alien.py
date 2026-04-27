'''
Program Name: Alien Invasion
Author: Henoc Cherestal
Purpose: Define the Alien class for the Alien Invasion game.
Starter Code: Based on the Alien Invasion project from class and
Python Crash Course, 3rd Edition by Eric Matthes.
Date: 04/27/2026
'''

import pygame
from pygame.sprite import Sprite

from settings import Settings


class Alien(Sprite):
    '''Represent a single alien in the fleet.'''

    def __init__(self, ai_game) -> None:
        '''Initialize the alien and set its starting position.'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings: Settings = ai_game.settings

        self.image = pygame.image.load(self.settings.alien_image).convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.image,
            (self.settings.alien_width, self.settings.alien_height),
        )
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)

    def check_edges(self) -> bool:
        '''Return True if the alien is at the edge of the screen.'''
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def update(self) -> None:
        '''Move the alien left or right.'''
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = int(self.x)