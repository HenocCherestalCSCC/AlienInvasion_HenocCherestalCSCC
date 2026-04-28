'''
Program Name: Alien Invasion
Author: Henoc Cherestal
Purpose: Create the custom HUD and scoreboard for Alien Invasion.
Starter Code: Based on the Alien Invasion project from class and
Python Crash Course, 3rd Edition by Eric Matthes.

Asset Attribution:
Font: Macondo
Author: John Vargas Beltrán
Source/Link: Google Fonts

Date: 04/28/2026
'''

import pygame


class Scoreboard:
    '''show the scoring information on the screen.'''

    def __init__(self, ai_game) -> None:
        '''Initialize scorekeeping attributes.'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.font = pygame.font.Font(
            str(self.settings.font_path),
            self.settings.font_size,
        )

        self.prep_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self) -> None:
        '''Turn the score into an actual rendered image.'''
        score_str = f"SCORE {self.stats.score:,}"
        self.score_image = self.font.render(
            score_str,
            True,
            self.settings.hud_text_color,
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = 40
        self.score_rect.top = 34

    def prep_level(self) -> None:
        '''Turn the level into a rendered image.'''
        level_str = f"LEVEL {self.stats.level}"
        self.level_image = self.font.render(
            level_str,
            True,
            self.settings.hud_text_color,
        )
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx
        self.level_rect.top = 34

    def prep_ships(self) -> None:
        '''Turn the ship count into a rendered image.'''
        ships_str = f"LIVES {self.stats.ships_left}"
        self.ships_image = self.font.render(
            ships_str,
            True,
            self.settings.hud_text_color,
        )
        self.ships_rect = self.ships_image.get_rect()
        self.ships_rect.right = self.screen_rect.right - 40
        self.ships_rect.top = 34

    def show_score(self) -> None:
        '''Draw the HUD and score information to the screen.'''
        hud_rect = pygame.Rect(20, 20, self.settings.screen_width - 40, 64)

        pygame.draw.rect(
            self.screen,
            self.settings.hud_bg_color,
            hud_rect,
            border_radius=14,
        )
        pygame.draw.rect(
            self.screen,
            self.settings.hud_border_color,
            hud_rect,
            width=2,
            border_radius=14,
        )

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ships_image, self.ships_rect)