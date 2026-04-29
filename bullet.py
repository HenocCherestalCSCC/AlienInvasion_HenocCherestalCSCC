'''
Program Name: Alien Invasion
Author: Henoc Cherestal
Purpose: Define the Bullet class for the Alien Invasion game.
Starter Code: Based on the Alien Invasion project from class and
Python Crash Course, 3rd Edition by Eric Matthes.
Date: 04/14/2026

Asset Attribution:
Laser Image: laserBlast.png
Author: Henoc Cherestal using AI-assisted image generation.
Source/Link: Local project asset at Assets/images/laserBlast.png

Laser Sound Layers:
Leaves Rustle 03 by TanwerAman
Sci Fi Gun Shot by SoundReality
Source/Link: Pixabay

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

        self.image = pygame.image.load(self.settings.bullet_image).convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.image,
            (self.settings.bullet_width, self.settings.bullet_height),
        )
        self.rect = self.image.get_rect()

        self.rect.midbottom = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self) -> None:
        '''Move the bullet up the screen.'''
        self.y -= self.settings.bullet_speed
        self.rect.y = int(self.y)

    def draw_bullet(self) -> None:
        '''Draw the bullet to the screen.'''
        self.screen.blit(self.image, self.rect)