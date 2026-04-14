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

from bullet import Bullet
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
        self.bullets = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

    def run_game(self) -> None:
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self) -> None:
        '''Respond to keypresses and window events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

                
    def _check_keydown_events(self, event: pygame.event.Event) -> None:
        '''Respond to key presses.'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event: pygame.event.Event) -> None:
        '''Respond to key releases.'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self) -> None:
        '''Redraw the screen during each pass through the loop.'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

    def _fire_bullet(self) -> None:
        '''Create a new bullet and add it to the bullets group.'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self) -> None:
        '''Update bullet positions and remove bullets off the screen.'''
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()