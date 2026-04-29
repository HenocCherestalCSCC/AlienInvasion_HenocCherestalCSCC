'''
Program Name: Alien Invasion
Author: Henoc Cherestal
Purpose: Run the Alien Invasion game.
Starter Code: Based on the Alien Invasion project from class and
Python Crash Course, 3rd Edition by Eric Matthes.
Date: 04/14/2026
'''

# Asset & Creative Process Disclosure:

# The visual identity of this project—including the custom ship, laser effects, and environmental backdrops—was developed through an iterative, 

# AI-assisted creative workflow. Rather than using online typical assets, I utilized AI as a foundational tool to explore specific silhouettes 
# and textures to build custom assets for Track 2.

# My process involved:

# Direction & Iteration: Engineering specific prompts to move beyond generic designs, ensuring a bespoke look for the player ship and weaponry.

# Curation & Selection: Evaluating hundreds of generations to hand-pick assets that maintained a cohesive "visual language" across the game.

# Refinement & Preparation: Manually post-processing and polishing the selected imagery to ensure technical compatibility, proper transparency, 
# and seamless integration within the game engine.

# The final result represents a deliberate fusion of generative technology and human creative direction, tailored specifically
# to bring the world I envisioned to life.

import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet
from settings import Settings
from ship import Ship
from sound_manager import SoundManager
from scoreboard import Scoreboard
from game_stats import GameStats
from button import Button


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
        
        self.background = self._load_background()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.sound = SoundManager(self)
        self.play_button = Button(self, "PLAY")

        self._create_fleet()


    def _load_background(self) -> pygame.Surface:
        '''Load and scale the background image.'''
        background = pygame.image.load(self.settings.background_image).convert()
        background = pygame.transform.scale(
            background,
            (self.settings.screen_width, self.settings.screen_height),
        )
        return background

    def _swarm_layout(self) -> list[tuple[int, int]]:
        '''Return the offsets for the insect-like fleet pattern.'''
        return [
            (0, 0),
            (-2, 1), (1, 1),
            (-4, 2), (-1, 2), (2, 2), (4, 2),
            (-5, 3), (-2, 3), (0, 3), (3, 3), (5, 3),
            (-4, 4), (-1, 4), (2, 4), (4, 4),
            (-3, 5), (0, 5), (3, 5),
            (-1, 6), (1, 6),
        ]

    def _create_fleet(self) -> None:
        '''Create the full alien fleet in a custom swarm pattern.'''
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        start_x = self.screen.get_rect().centerx - (alien_width // 2)
        start_y = 80

        for column_offset, row_offset in self._swarm_layout():
            self._create_alien(
                start_x,
                start_y,
                column_offset,
                row_offset,
                alien_width,
                alien_height,
            )

    def _create_alien(
        self,
        start_x: int,
        start_y: int,
        column_offset: int,
        row_offset: int,
        alien_width: int,
        alien_height: int,
    ) -> None:
        '''Create a single alien and place it in the fleet.'''
        alien = Alien(self)

        x_spacing = alien_width - 8
        y_spacing = alien_height - 14

        alien.rect.x = start_x + (column_offset * x_spacing)
        alien.rect.y = start_y + (row_offset * y_spacing)
        alien.x = float(alien.rect.x)

        self.aliens.add(alien)    

    def run_game(self) -> None:
        '''Start the main loop for the game.'''
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos) 

    def _check_play_button(self, mouse_pos: tuple[int, int]) -> None:
        '''Start a new game when the player clicks Play.'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _start_game(self) -> None:
        '''Start a fresh game.'''
        self.stats.reset_stats()
        self.stats.game_active = True

        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        self.bullets.empty()
        self.aliens.empty()
        self._create_fleet()
        self.ship.center_ship()

        pygame.mouse.set_visible(False)
        self.sound.play_music()               

                
    def _check_keydown_events(self, event: pygame.event.Event) -> None:
        '''Respond to key presses.'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.stats.game_active:
            self._start_game()
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
        self.screen.blit(self.background, (0, 0))
        self.ship.blitme()
        self.aliens.draw(self.screen)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.blitme()

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

        self._check_bullet_alien_collisions()        

    def _check_bullet_alien_collisions(self) -> None:
        '''Respond to bullet and alien collisions.'''
        collisions = pygame.sprite.groupcollide(
            self.bullets,
            self.aliens,
            True,
            True,
        )

        if collisions:
            self.sound.play_impact()

            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)

            self.sb.prep_score()

        if not self.aliens:
            self.bullets.empty()
            self.stats.level += 1
            self.sb.prep_level()
            self._create_fleet()


    def _update_aliens(self) -> None:
        '''Update the positions of all aliens in the fleet.'''
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _check_fleet_edges(self) -> None:
        '''Respond appropriately if any aliens have reached an edge.'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) -> None:
        '''Drop the fleet and change the fleet's direction.'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _ship_hit(self) -> None:
        '''Respond to the ship being hit by an alien.'''
        self.sound.play_impact()

        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.ships_left = 0
            self.sb.prep_ships()
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            self.sound.stop_music()

    def _check_aliens_bottom(self) -> None:
        '''Check whether any aliens have reached the bottom of the screen.'''
        screen_rect = self.screen.get_rect()

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break    

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()