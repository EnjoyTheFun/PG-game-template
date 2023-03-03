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
        """Function that creates the controllable unit."""
        self.player_unit = Unit(position, size, speed, self.assets.TEST_ASSET)
        self.units.add(self.player_unit)

    def draw_objects(self):
        """Function that draws all objects."""
        # You have to 'refresh' the state of the screen so you dont draw on top
        # of each draw execution. Simplest way is to just recolor everything back
        # to the default background color.
        self.surface.fill(pygame.Color('black'))
        # Draw each unit
        for unit in self.units:
            unit.draw(self.surface)

    def handle_movement(self):
        """Function that manages the input for movement actions."""
        keys = pygame.key.get_pressed()
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
            # If main window was closed
            if event.type == QUIT:
                pygame.quit()
                exit()
            # If mouse button was pressed   
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
            # If keyboard key was pressed        
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    print('Space pressed. Spawning new unit!')
                    # You can spawn more units if you like :)
                    self.spawn_goal_unit()
                # If key combination was pressed
                elif event.key == K_r and pygame.key.get_mods() & KMOD_CTRL:
                    print('Key combination CTRL+R pressed.')

    def spawn_goal_unit(self):
        """Function that creates the goal unit at random position."""
        # get the size of the player unit
        u_width = self.player_unit.rect.width
        u_height = self.player_unit.rect.height
        
        rand_x = random.randrange(0, WINDOW_WIDTH - u_width)
        rand_y = random.randrange(0, WINDOW_HEIGHT - u_height)
        # if selected goal position is already colliding with the player_unit
        # generate new one and check again
        while self.player_unit.rect.colliderect((rand_x, rand_y),
                                                (u_width/2, u_height/2)):
            rand_x = random.randrange(0, WINDOW_WIDTH - u_width)
            rand_y = random.randrange(0, WINDOW_HEIGHT - u_height)
        
        # create custom surface    
        surf = pygame.Surface((u_width/2, u_height/2))
        # fill surface with color
        surf.fill(pygame.Color('firebrick2'))
        # set opacity of the surface (255=None)
        surf.set_alpha(150)
        # add the newly created unit to the units list
        self.units.add(Unit((rand_x, rand_y), u_width/2, 0, surf))

    def unit_collide(self):
        """Function that checks for collision between unit objects."""
        for unit in self.units:
            # ensure that player_unit is not checking for collision with self
            if unit is not self.player_unit and self.player_unit.rect.colliderect(unit.rect):
                # destroy colliding unit
                unit.kill()
                # increment score
                self.player.score += 1
                # spawn next unit
                self.spawn_goal_unit()
