from pygame.sprite import Sprite
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
import pygame


class Unit(Sprite):
    """Class that represents units in the game"""

    def __init__(self, coords, size, speed, asset):
        super().__init__()

        self.movement_speed = speed
        self.rect = pygame.Rect(coords[0], coords[1], size, size)
        self.asset = asset

    def move(self, direction_vector):
        """Function that allows the movement of the unit based on a 2D vector."""
        direction_vector.scale_to_length(self.movement_speed)
        # move in place (which means move from the current position)
        self.rect.move_ip(direction_vector)
        self._clamp_pos()

    def _clamp_pos(self):
        """Function that sets boundries for the unit's position based on the window size."""
        # Can also use rect.update()
        self.rect.x = max(0, min(self.rect.x, WINDOW_WIDTH-self.rect.width))
        self.rect.y = max(0, min(self.rect.y, WINDOW_HEIGHT-self.rect.height))

    def draw(self, surface):
        """Function that draws the object's asset on specified surface."""
        surface.blit(self.asset, self.rect)
        # Draw hitbox (for debug purposes)
        # pygame.draw.rect(surface, pygame.Color('cyan'), self.rect, width=1)
