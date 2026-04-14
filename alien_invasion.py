'''
Program Name: Alien Invasion
Author: Henoc Cherestal
Purpose: Run the Alien Invasion game.
Starter Code: Based on the Alien Invasion project from class and
Python Crash Course, 3rd Edition by Eric Matthes.
Date: 04/14/2026
'''


import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self) -> None:
        '''Initialize the game and create game resources.'''
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.caption)

        self.ship = Ship(self)
        self.clock = pygame.time.Clock()

    def run_game(self) -> None:
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self) -> None:
        '''Respond to keypresses and window events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def _update_screen(self) -> None:
        '''Redraw the screen during each pass through the loop.'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()