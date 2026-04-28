'''
Program Name: Alien Invasion
Author: Henoc Cherestal
Purpose: Manage custom music and sound effects for Alien Invasion.
Starter Code: Based on the Alien Invasion project from class and
Python Crash Course, 3rd Edition by Eric Matthes.

Asset Attribution:
Background Music: backgroundMusic.mp3
Author: Musinova
Source/Link: https://pixabay.com/users/musinova-47643763/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=444655

Laser Sound Layer 1: Leaves Rustle 03
Author: TanwerAman
Source/Link: Pixabay

Laser Sound Layer 2: Sci Fi Gun Shot
Author: SoundReality
Source/Link: Pixabay

Impact Sound: impactSound.mp3
Author: floraphonic
Source/Link: Pixabay

Date: 04/28/2026
'''

import pygame


class SoundManager:
    '''Manage game music and layered sound effects.'''

    def __init__(self, ai_game) -> None:
        '''Load the sounds used in the game.'''
        self.settings = ai_game.settings
        self.sound_ready = True

        try:
            pygame.mixer.init()

            self.leaves_sound = pygame.mixer.Sound(
                str(self.settings.leaves_sound)
            )
            self.gun_sound = pygame.mixer.Sound(
                str(self.settings.gun_sound)
            )
            self.impact_sound = pygame.mixer.Sound(
                str(self.settings.impact_sound)
            )

            self.leaves_sound.set_volume(0.35)
            self.gun_sound.set_volume(0.45)
            self.impact_sound.set_volume(0.55)

        except pygame.error:
            self.sound_ready = False
            self.leaves_sound = None
            self.gun_sound = None
            self.impact_sound = None

    def play_music(self) -> None:
        '''Start the background music if sound is ready.'''
        if self.sound_ready and self.settings.music_file.exists():
            pygame.mixer.music.load(str(self.settings.music_file))
            pygame.mixer.music.set_volume(0.25)
            pygame.mixer.music.play(-1)

    def stop_music(self) -> None:
        '''Stop the background music.'''
        if self.sound_ready:
            pygame.mixer.music.stop()

    def play_laser(self) -> None:
        '''Play the layered laser sound.'''
        if self.sound_ready:
            if self.leaves_sound:
                self.leaves_sound.play()
            if self.gun_sound:
                self.gun_sound.play()

    def play_impact(self) -> None:
        '''Play the impact sound.'''
        if self.sound_ready and self.impact_sound:
            self.impact_sound.play()