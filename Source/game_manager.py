import pygame
from Source.Models.unit import Unit
from Source.Models.player import Player
from pygame.locals import (QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_SPACE, K_r,
                           KMOD_CTRL, K_w, K_UP, K_s, K_DOWN, K_a, K_LEFT,
                           K_d, K_RIGHT)
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
import random


class GameManager():
    """A class that contains the game's main logic."""

    def __init__(self, surface, assets):
        self.surface = surface
        self.player = Player()
        self.assets = assets
        self.units = pygame.sprite.Group()

    def spawn_player_unit(self, position, size, speed):
        self.player_unit = Unit(position, size, speed, self.assets.TEST_ASSET)
        self.units.add(self.player_unit)

    def update_objects(self):
        self.surface.fill(pygame.Color('black'))
        for unit in self.units:
            unit.draw(self.surface)

    def handle_movement(self):
        keys = pygame.key.get_pressed()  # checking pressed keys
        if (keys[K_UP] or keys[K_w]):
            self.player_unit.move(pygame.Vector2(0, -1))
        if keys[K_DOWN] or keys[K_s]:
            self.player_unit.move(pygame.Vector2(0, 1))
        if keys[K_LEFT] or keys[K_a]:
            self.player_unit.move(pygame.Vector2(-1, 0))
        if keys[K_RIGHT] or keys[K_d]:
            self.player_unit.move(pygame.Vector2(1, 0))

    def handle_events(self):
        """Function that does the event handling."""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouseXY = pygame.mouse.get_pos()
                if event.button == 1:
                    print('Left mouse button click.')
                elif event.button == 2:
                    print('Middle mouse button click.')
                elif event.button == 3:
                    print('Right mouse button click.')
                else:
                    print(mouseXY)
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    print('Space pressed.')
                    self.spawn_goal_unit()
                elif event.key == K_r and pygame.key.get_mods() & KMOD_CTRL:
                    print('Key combination CTRL+R pressed.')

    def spawn_goal_unit(self):
        u_width = self.assets.TEST_ASSET.get_width()
        u_height = self.assets.TEST_ASSET.get_height()
        rand_x = random.randrange(0, WINDOW_WIDTH - u_width)
        rand_y = random.randrange(0, WINDOW_HEIGHT - u_height)
        while self.player_unit.rect.colliderect((rand_x, rand_y),
                                                (u_width/2, u_height/2)):
            rand_x = random.randrange(0, WINDOW_WIDTH - u_width)
            rand_y = random.randrange(0, WINDOW_HEIGHT - u_height)
        surf = pygame.Surface((u_width/2, u_height/2))
        surf.fill(pygame.Color('firebrick2'))
        self.units.add(Unit((rand_x, rand_y), u_width/2, 0, surf))

    def unit_collide(self):
        for unit in self.units:
            if unit is not self.player_unit and self.player_unit.rect.colliderect(unit.rect):
                unit.kill()
                self.player.score += 1
                self.spawn_goal_unit()
