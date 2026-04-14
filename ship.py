'''
Program Name: Alien Invasion
Author: Henoc Cherestal
Purpose: Define the Ship class for the Alien Invasion game.
Starter Code: Based on the Alien Invasion project from class and
Python Crash Course, 3rd Edition by Eric Matthes.
Date: 04/14/2026
'''

import pygame

from settings import Settings


class Ship:
    '''Manage the player's ship.'''

    def __init__(self, ai_game) -> None:
        '''Initialize the ship and set its starting position.'''
        self.screen = ai_game.screen
        self.settings: Settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_image).convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_width, self.settings.ship_height),
        )
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 10

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def blitme(self) -> None:
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)

    def update(self) -> None:
        '''Update the ship's position based on movement flags.'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = int(self.x)

    def center_ship(self) -> None:
        '''Center the ship on the bottom of the screen.'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 10
        self.x = float(self.rect.x)