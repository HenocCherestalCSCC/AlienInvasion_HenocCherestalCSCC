'''
Program Name: Alien Invasion
Author: Henoc Cherestal
Purpose: Create the custom Play button for Alien Invasion.
Starter Code: Based on the Alien Invasion project from class and
Python Crash Course, 3rd Edition by Eric Matthes.

Asset Attribution:
Play Button Image: playButton.png
Author: Henoc Cherestal using AI-assisted image generation.
Source/Link: Local project asset at Assets/images/playButton.png

Font: Macondo Swash Caps
Author: John Vargas Beltrán
Source/Link: Google Fonts

Date: 04/28/2026
'''

import pygame


class Button:
    '''Create a custom image button with text on top.'''

    def __init__(self, ai_game, msg: str) -> None:
        '''Initialize button attributes.'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load(
            str(self.settings.play_button_image)
        ).convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.image,
            (self.settings.button_width, self.settings.button_height),
        )
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.font = pygame.font.Font(
            str(self.settings.button_font_path),
            self.settings.button_font_size,
        )
        self._prep_msg(msg)

    def _prep_msg(self, msg: str) -> None:
        '''Turn the button message into a rendered image.'''
        self.msg_image = self.font.render(
            msg,
            True,
            self.settings.button_text_color,
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def blitme(self) -> None:
        '''Draw the button image and text.'''
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)