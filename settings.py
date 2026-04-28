'''
Program Name: Alien Invasion
Author: Henoc Cherestal
Purpose: Store the settings for the Alien Invasion game.
Starter Code: Based on the Alien Invasion project from class and
Python Crash Course, 3rd Edition by Eric Matthes.
Date: 04/14/2026

Asset Attribution:
Font: Macondo and Macondo Swash Caps
Author: John Vargas Beltrán
Source/Link: Google Fonts

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

        self.ships_limit = 3
        self.alien_points = 50

        self.hud_text_color = (220, 255, 225)
        self.hud_bg_color = (12, 28, 24)
        self.hud_border_color = (105, 220, 170)

        self.button_width = 260
        self.button_height = 100
        self.button_text_color = (245, 255, 230)

        self.font_size = 28
        self.button_font_size = 42

        self.base_dir = Path(__file__).resolve().parent
        self.assets_dir = self.base_dir / "Assets"
        self.images_dir = self.assets_dir / "images"
        self.fonts_dir = self.assets_dir / "Fonts" / "Macondo"
        self.sound_dir = self.assets_dir / "sound"

        self.ship_image = self.images_dir / "ship.png"
        self.bullet_image = self.images_dir / "laserBlast.png"
        self.background_image = self.images_dir / "Starbasesnow.png"
        self.alien_image = self.images_dir / "alien.png"
        self.play_button_image = self.images_dir / "playButton.png"

        self.font_path = self.fonts_dir / "Macondo-Regular.ttf"
        self.button_font_path = self.fonts_dir / "MacondoSwashCaps-Regular.ttf"

        self.music_file = self.sound_dir / "backgroundMusic.mp3"
        self.leaves_sound = self.sound_dir / "leavesRustle03.mp3"
        self.gun_sound = self.sound_dir / "sciFiGunShot.mp3"
        self.impact_sound = self.sound_dir / "impactSound.mp3"