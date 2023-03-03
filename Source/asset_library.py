import pygame
import os


class AssetLibrary():
    """Class that holds references to all assets that are used in the game."""

    def __init__(self, path_to_files):
        self.path = path_to_files
        self._load_all_assets()

    def _load_all_assets(self):
        self.TEST_ASSET = pygame.image.load(os.path.join(
            self.path, 'Assets', 'Images', 'test.png'))

    def optimize_all_assets(self):
        # Use convert_alpha() to preserve transparency if necessary
        self.TEST_ASSET = self.TEST_ASSET.convert()
